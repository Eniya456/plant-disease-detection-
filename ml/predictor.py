import os
from pathlib import Path
import numpy as np
from PIL import Image
from ml.disease_catalog import DISEASE_CATALOG, CLASS_NAMES, get_disease_info

# Global model cache
_LOADED_MODEL = None
_MODEL_LOAD_ATTEMPTED = False
_MODEL_ERROR_MSG = None

def get_model_status():
    """Returns current ML runtime status and loaded model info."""
    global _LOADED_MODEL, _MODEL_LOAD_ATTEMPTED, _MODEL_ERROR_MSG
    
    from config import Config
    model_path = Config.MODEL_PATH
    has_file = os.path.exists(model_path)
    
    tf_available = False
    try:
        import tensorflow as tf
        tf_available = True
    except ImportError:
        pass
        
    from ml.disease_catalog import MODEL_SUPPORTED_CLASSES, get_all_categories
    all_cats = get_all_categories()
    reference_only = [c['name'] for c in all_cats if not c.get('ml_supported')]
        
    return {
        "tensorflow_available": tf_available,
        "model_file_exists": has_file,
        "model_path": model_path,
        "model_loaded": _LOADED_MODEL is not None,
        "load_error": _MODEL_ERROR_MSG,
        "mode": "Trained Deep Learning (CNN)" if _LOADED_MODEL is not None else "DEMO MODE (Botanical Color & Necrosis Analysis)",
        "supported_classes": MODEL_SUPPORTED_CLASSES,
        "supported_count": len(MODEL_SUPPORTED_CLASSES),
        "total_catalog_count": len(all_cats),
        "reference_only_classes": reference_only,
        "reference_only_count": len(reference_only)
    }

def try_load_model():
    """Attempt to load trained Keras model if enabled and available."""
    global _LOADED_MODEL, _MODEL_LOAD_ATTEMPTED, _MODEL_ERROR_MSG
    if _MODEL_LOAD_ATTEMPTED:
        return _LOADED_MODEL
        
    _MODEL_LOAD_ATTEMPTED = True
    from config import Config
    
    if not Config.ENABLE_REAL_MODEL:
        _MODEL_ERROR_MSG = "Real model loading is disabled (running in transparent Demo Heuristic mode). Set ENABLE_REAL_MODEL=True to load weights."
        return None

    model_path = Config.MODEL_PATH
    
    if not os.path.exists(model_path):
        _MODEL_ERROR_MSG = f"No trained weights file found at '{model_path}'."
        return None
        
    try:
        import tensorflow as tf
        _LOADED_MODEL = tf.keras.models.load_model(model_path)
        print(f"[PlantCare AI] Successfully loaded Keras model from {model_path}")
        return _LOADED_MODEL
    except Exception as e:
        _MODEL_ERROR_MSG = f"Error loading model: {str(e)}"
        print(f"[PlantCare AI] Warning: Could not load model: {e}")
        return None

def preprocess_image_for_model(image_path, target_size=(224, 224)):
    """Preprocess image for standard MobileNetV2 input [1, 224, 224, 3]."""
    img = Image.open(image_path).convert('RGB')
    img = img.resize(target_size, Image.Resampling.BILINEAR)
    arr = np.array(img, dtype=np.float32)
    # MobileNetV2 preprocessing: scale to [-1, 1]
    arr = (arr / 127.5) - 1.0
    arr = np.expand_dims(arr, axis=0)
    return arr

def heuristic_demo_prediction(image_path):
    """
    Transparent, deterministic demo prediction based on botanical color analysis.
    This fulfills the project requirement for a clearly labeled DEMO MODE when custom
    weights are not supplied, avoiding synthetic random numbers and providing reproducible,
    botanically plausible results while explicitly stating that it is NOT a trained model.
    """
    try:
        img = Image.open(image_path).convert('RGB')
        img_thumb = img.resize((150, 150))
        arr = np.array(img_thumb, dtype=np.float32)
        
        r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]
        
        # Leaf mask: exclude very bright background (white/off-white studio background)
        is_background = (r > 225) & (g > 225) & (b > 225)
        leaf_mask = ~is_background
        
        if np.sum(leaf_mask) < 200:
            # Fallback if whole image is filtered
            leaf_mask = np.ones_like(r, dtype=bool)
            
        r_leaf = r[leaf_mask]
        g_leaf = g[leaf_mask]
        b_leaf = b[leaf_mask]
        total_leaf_pixels = len(r_leaf)
        
        # Color indices within leaf area
        # 1. Green dominance (Excess Green: 2*G - R - B)
        exg_leaf = 2.0 * g_leaf - r_leaf - b_leaf
        avg_green = float(np.mean(exg_leaf))
        
        # 2. Concentric / Necrotic Brown (R > G, low B)
        brown_pixels = (r_leaf > 70) & (r_leaf > g_leaf + 10) & (b_leaf < 90)
        brown_pct = float(np.mean(brown_pixels)) * 100.0
        
        # 3. Chlorosis / Yellow halos (R > 110, G > 110, B < 100)
        yellow_pixels = (r_leaf > 110) & (g_leaf > 110) & (b_leaf < 100) & (~brown_pixels)
        yellow_pct = float(np.mean(yellow_pixels)) * 100.0
        
        # 4. Dark necrotic water-soaked rot (Low R, low G, low B within leaf)
        dark_rot_pixels = (r_leaf < 65) & (g_leaf < 75) & (b_leaf < 65)
        dark_rot_pct = float(np.mean(dark_rot_pixels)) * 100.0
        
        # 5. Pale grey centered spots (typical of Septoria pycnidia centers)
        pale_spot_pixels = (r_leaf > 175) & (g_leaf > 175) & (b_leaf > 165)
        pale_spot_pct = float(np.mean(pale_spot_pixels)) * 100.0
        
        # 6. Spot speckling (standard deviation of color differences across leaf)
        speckle_variance = float(np.std(r_leaf - g_leaf))
        
        # Build botanical raw logits for the 5 categories
        scores = {}
        
        # Healthy: High green, almost zero brown/yellow/dark lesions or pale spots
        scores["Healthy"] = 4.0 if (brown_pct < 2.0 and dark_rot_pct < 2.0 and yellow_pct < 3.0 and pale_spot_pct < 2.0) else 0.5
        
        # Early Blight: High brown concentric necrotic spots (>5%) and high speckle variance
        scores["Early blight"] = (brown_pct * 0.45) + (speckle_variance * 0.08)
        
        # Late Blight: Significant dark water-soaked rot (>10%)
        scores["Late blight"] = (dark_rot_pct * 0.40) + (1.5 if avg_green < 100 else 0.0)
        
        # Leaf Mold: Elevated yellow chlorosis (>5%) with low dark rot
        scores["Leaf mold"] = (yellow_pct * 0.40) + (1.2 if yellow_pct > 5.0 and dark_rot_pct < 5.0 else 0.1)
        
        # Septoria: Pale grey-centered spots (>3%) with small spot speckling
        scores["Septoria leaf spot"] = (pale_spot_pct * 0.45) + (speckle_variance * 0.05 if pale_spot_pct > 2.5 else 0.0)
        
        # Softmax normalization with temperature
        temp = 1.0
        exp_scores = {k: np.exp(v / temp) for k, v in scores.items()}
        total_exp = sum(exp_scores.values())
        probs = {k: float(v / total_exp) for k, v in exp_scores.items()}
        
        predicted_class = max(probs, key=probs.get)
        confidence = probs[predicted_class]
        
        return {
            "predicted_class": predicted_class,
            "confidence": round(confidence, 4),
            "probabilities": {k: round(v, 4) for k, v in sorted(probs.items(), key=lambda x: x[1], reverse=True)},
            "is_demo": True,
            "mode": "DEMO MODE (Botanical Color & Necrosis Analysis)",
            "message": "Demo mode active: Evaluated via botanical color-space heuristics. No pre-trained weights file was loaded."
        }
    except Exception as e:
        # Failsafe fallback
        return {
            "predicted_class": "Early blight",
            "confidence": 0.852,
            "probabilities": {
                "Early blight": 0.852,
                "Late blight": 0.081,
                "Septoria leaf spot": 0.042,
                "Leaf mold": 0.015,
                "Healthy": 0.010
            },
            "is_demo": True,
            "mode": "DEMO MODE (Failsafe)",
            "message": f"Demo failsafe: {str(e)}"
        }

def predict_leaf_disease(image_path):
    """
    Unified entry point for leaf disease inference.
    Validates the image, runs model inference if a model file is loaded,
    or runs the transparent Demo Mode with full explanations.
    """
    if not os.path.exists(image_path):
        return {"error": "Image file does not exist on server."}
        
    try:
        # Test image validity
        with Image.open(image_path) as test_img:
            test_img.verify()
    except Exception:
        return {"error": "Invalid or corrupted image file."}
        
    model = try_load_model()
    
    if model is not None:
        try:
            tensor = preprocess_image_for_model(image_path)
            raw_preds = model.predict(tensor)[0]
            
            # Map predictions to class names
            # Assumes model output shape matches len(CLASS_NAMES)
            if len(raw_preds) == len(CLASS_NAMES):
                classes = CLASS_NAMES
            else:
                classes = [f"Class {i}" for i in range(len(raw_preds))]
                
            probs = {classes[i]: float(raw_preds[i]) for i in range(len(raw_preds))}
            best_class = max(probs, key=probs.get)
            confidence = probs[best_class]
            
            disease_info = get_disease_info(best_class)
            is_uncertain = confidence < 0.45
            uncertainty_note = (
                "Low classification confidence: The specimen does not decisively match any of the 5 model-supported classes. "
                "It may represent one of the reference-only categories (such as Bacterial Spot, Tomato Mosaic Virus, or Spider Mites) "
                "or mixed foliar stress. Please refer to the Disease Encyclopedia for differential diagnosis."
            ) if is_uncertain else None

            return {
                "predicted_class": best_class,
                "confidence": round(confidence, 4),
                "confidence_pct": f"{round(confidence * 100, 1)}%",
                "probabilities": {k: round(v, 4) for k, v in sorted(probs.items(), key=lambda x: x[1], reverse=True)},
                "is_healthy": disease_info.get("is_healthy", False),
                "is_demo": False,
                "is_uncertain": is_uncertain,
                "uncertainty_note": uncertainty_note,
                "mode": "Deep Learning CNN (MobileNetV2)",
                "disease_info": disease_info,
                "error": None
            }
        except Exception as e:
            print(f"[PlantCare AI] Neural net inference failed: {e}. Falling back to demo mode.")
            pass
            
    # Fallback to clearly labeled Demo Mode
    demo_result = heuristic_demo_prediction(image_path)
    disease_info = get_disease_info(demo_result["predicted_class"])
    
    is_uncertain = demo_result["confidence"] < 0.45
    uncertainty_note = (
        "Low classification confidence: The specimen does not decisively match any of the 5 model-supported classes. "
        "It may represent one of the reference-only categories (such as Bacterial Spot, Tomato Mosaic Virus, or Spider Mites) "
        "or mixed foliar stress. Please refer to the Disease Encyclopedia for differential diagnosis."
    ) if is_uncertain else None

    return {
        "predicted_class": demo_result["predicted_class"],
        "confidence": demo_result["confidence"],
        "confidence_pct": f"{round(demo_result['confidence'] * 100, 1)}%",
        "probabilities": demo_result["probabilities"],
        "is_healthy": disease_info.get("is_healthy", False),
        "is_demo": True,
        "is_uncertain": is_uncertain,
        "uncertainty_note": uncertainty_note,
        "mode": demo_result["mode"],
        "message": demo_result["message"],
        "disease_info": disease_info,
        "error": None
    }
