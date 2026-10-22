/**
 * PlantCare AI - Main JavaScript
 * Handles drag-and-drop, image preview, async loading feedback, and UI interactions.
 */

document.addEventListener('DOMContentLoaded', function () {
    // ----------------------------------------------------
    // 1. Mobile Sidebar Toggle
    // ----------------------------------------------------
    const sidebarToggle = document.getElementById('sidebarToggle');
    const sidebar = document.querySelector('.sidebar');
    const backdrop = document.querySelector('.sidebar-backdrop');

    if (sidebarToggle && sidebar) {
        sidebarToggle.addEventListener('click', function () {
            sidebar.classList.toggle('show');
            if (backdrop) backdrop.classList.toggle('show');
        });
    }

    if (backdrop) {
        backdrop.addEventListener('click', function () {
            sidebar.classList.remove('show');
            backdrop.classList.remove('show');
        });
    }

    // ----------------------------------------------------
    // 2. Drag and Drop & Image Preview (Detect Page)
    // ----------------------------------------------------
    const dropzone = document.getElementById('uploadDropzone');
    const fileInput = document.getElementById('imageFileInput');
    const previewContainer = document.getElementById('previewContainer');
    const previewImage = document.getElementById('previewImage');
    const uploadPrompt = document.getElementById('uploadPrompt');
    const submitBtn = document.getElementById('submitScanBtn');
    const resetBtn = document.getElementById('resetUploadBtn');
    const uploadForm = document.getElementById('detectionForm');
    const loadingOverlay = document.getElementById('loadingOverlay');
    const loadingStatusText = document.getElementById('loadingStatusText');
    const errorMessage = document.getElementById('uploadErrorMessage');

    function showError(msg) {
        if (errorMessage) {
            errorMessage.textContent = msg;
            errorMessage.classList.remove('d-none');
        } else {
            alert(msg);
        }
    }

    function clearError() {
        if (errorMessage) {
            errorMessage.classList.add('d-none');
            errorMessage.textContent = '';
        }
    }

    function handleFile(file) {
        clearError();
        if (!file) return;

        // Validate type
        const validTypes = ['image/jpeg', 'image/jpg', 'image/png', 'image/webp'];
        if (!validTypes.includes(file.type.toLowerCase()) && !/\.(jpe?g|png|webp)$/i.test(file.name)) {
            showError('Invalid file type! Please upload a JPG, JPEG, PNG, or WEBP leaf image.');
            return;
        }

        // Validate size (max 8MB)
        if (file.size > 8 * 1024 * 1024) {
            showError('File is too large! Maximum allowed image size is 8 MB.');
            return;
        }

        const reader = new FileReader();
        reader.onload = function (e) {
            if (previewImage) {
                previewImage.src = e.target.result;
            }
            if (uploadPrompt) uploadPrompt.classList.add('d-none');
            if (previewContainer) previewContainer.classList.remove('d-none');
            if (submitBtn) submitBtn.disabled = false;
            if (resetBtn) resetBtn.classList.remove('d-none');
        };
        reader.readAsDataURL(file);
    }

    if (dropzone && fileInput) {
        dropzone.addEventListener('click', function (e) {
            if (e.target !== resetBtn && !resetBtn?.contains(e.target)) {
                fileInput.click();
            }
        });

        fileInput.addEventListener('change', function () {
            if (this.files && this.files[0]) {
                handleFile(this.files[0]);
            }
        });

        ['dragenter', 'dragover'].forEach(eventName => {
            dropzone.addEventListener(eventName, function (e) {
                e.preventDefault();
                e.stopPropagation();
                dropzone.classList.add('dragover');
            }, false);
        });

        ['dragleave', 'drop'].forEach(eventName => {
            dropzone.addEventListener(eventName, function (e) {
                e.preventDefault();
                e.stopPropagation();
                dropzone.classList.remove('dragover');
            }, false);
        });

        dropzone.addEventListener('drop', function (e) {
            const dt = e.dataTransfer;
            const files = dt.files;
            if (files && files[0]) {
                fileInput.files = files;
                handleFile(files[0]);
            }
        });
    }

    if (resetBtn) {
        resetBtn.addEventListener('click', function (e) {
            e.stopPropagation();
            if (fileInput) fileInput.value = '';
            if (previewImage) previewImage.src = '';
            if (previewContainer) previewContainer.classList.add('d-none');
            if (uploadPrompt) uploadPrompt.classList.remove('d-none');
            if (submitBtn) submitBtn.disabled = true;
            resetBtn.classList.add('d-none');
            clearError();
        });
    }

    // ----------------------------------------------------
    // 3. Sample Leaves Click-to-Test
    // ----------------------------------------------------
    const sampleCards = document.querySelectorAll('.sample-leaf-card');
    const sampleNameInput = document.getElementById('sampleNameInput');

    sampleCards.forEach(card => {
        card.addEventListener('click', async function () {
            const imgPath = this.getAttribute('data-img-src');
            const sampleName = this.getAttribute('data-name');
            if (!imgPath) return;

            // Highlight chosen card
            sampleCards.forEach(c => c.classList.remove('border-success', 'bg-success-subtle'));
            this.classList.add('border-success', 'bg-success-subtle');

            if (sampleNameInput) {
                // Map to actual sample image filename on server
                const fileMap = {
                    'healthy_sample.jpg': 'healthy_leaf.jpg',
                    'early_blight_sample.jpg': 'early_blight_leaf.jpg',
                    'late_blight_sample.jpg': 'late_blight_leaf.jpg',
                    'leaf_mold_sample.jpg': 'leaf_mold_leaf.jpg',
                    'septoria_sample.jpg': 'septoria_leaf.jpg'
                };
                sampleNameInput.value = fileMap[sampleName] || sampleName;
            }

            try {
                const response = await fetch(imgPath);
                const blob = await response.blob();
                const file = new File([blob], sampleName || 'sample_leaf.jpg', { type: blob.type || 'image/jpeg' });
                
                const dataTransfer = new DataTransfer();
                dataTransfer.items.add(file);
                if (fileInput) {
                    fileInput.files = dataTransfer.files;
                    handleFile(file);
                }
            } catch (err) {
                console.warn("DataTransfer fallback:", err);
                // Fallback: set preview image directly
                if (previewImage) previewImage.src = imgPath;
                if (uploadPrompt) uploadPrompt.classList.add('d-none');
                if (previewContainer) previewContainer.classList.remove('d-none');
                if (submitBtn) submitBtn.disabled = false;
                if (resetBtn) resetBtn.classList.remove('d-none');
            }
        });
    });

    // ----------------------------------------------------
    // 4. Form Submit & Loading Progression
    // ----------------------------------------------------
    if (uploadForm) {
        uploadForm.addEventListener('submit', function (e) {
            if (!fileInput || !fileInput.files || fileInput.files.length === 0) {
                e.preventDefault();
                showError('Please select or drag-and-drop a plant leaf image first.');
                return;
            }

            if (loadingOverlay) {
                loadingOverlay.classList.remove('d-none');
                if (submitBtn) submitBtn.disabled = true;

                const messages = [
                    "Uploading leaf specimen to secure cloud pipeline...",
                    "Preprocessing image matrix (224x224 RGB normalization)...",
                    "Executing Convolutional Feature Extraction...",
                    "Computing Softmax class probabilities...",
                    "Retrieving agronomic pathology advisory..."
                ];
                let msgIdx = 0;
                setInterval(() => {
                    if (msgIdx < messages.length - 1 && loadingStatusText) {
                        msgIdx++;
                        loadingStatusText.textContent = messages[msgIdx];
                    }
                }, 750);
            }
        });
    }

    // ----------------------------------------------------
    // 5. Prediction History Table Search
    // ----------------------------------------------------
    const historySearch = document.getElementById('historySearchInput');
    if (historySearch) {
        historySearch.addEventListener('keyup', function () {
            const query = this.value.toLowerCase();
            const rows = document.querySelectorAll('#historyTableBody tr');
            rows.forEach(row => {
                const text = row.textContent.toLowerCase();
                row.style.display = text.includes(query) ? '' : 'none';
            });
        });
    }

    // ----------------------------------------------------
    // 6. Auto-dismiss alerts after 5 seconds
    // ----------------------------------------------------
    const autoAlerts = document.querySelectorAll('.alert-dismissible');
    autoAlerts.forEach(alertEl => {
        setTimeout(() => {
            const closeBtn = alertEl.querySelector('.btn-close');
            if (closeBtn) closeBtn.click();
        }, 5000);
    });
});
