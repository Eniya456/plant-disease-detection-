"""
PlantCare AI — Comprehensive Botanical Disease & Pathology Catalog
Structured Tomato Foliar Categories (Diseases, Pests, Physiological & Uncertain Conditions)
"""

DISEASE_CATALOG = {
    "healthy": {
        "id": "healthy",
        "name": "Healthy Tomato Leaf",
        "scientific_name": "Solanum lycopersicum (Healthy)",
        "category": "healthy",
        "category_label": "Healthy Foliage",
        "ml_supported": True,
        "is_healthy": True,
        "severity": "None (Optimum Vegetative Vigor)",
        "badge_color": "success",
        "description": "The leaf exhibits uniform green chlorophyll pigmentation with intact tissue, no lesions, necrosis, chlorosis, or fungal sporulation.",
        "symptoms": [
            "Vibrant, even green coloration across entire blade",
            "Smooth leaf surface with intact cellular structure",
            "No brown, yellow, water-soaked spotting, or stippling",
            "Normal turgidity, leaf architecture, and vein vascularization"
        ],
        "favorable_conditions": "Balanced soil fertility, appropriate diurnal temperatures (18-28°C), adequate sunlight, and controlled root-zone hydration.",
        "causes": "Optimal environmental conditions, balanced soil fertility, adequate sunlight, and effective pest management.",
        "prevention": [
            "Continue standard drip irrigation avoiding canopy leaf wetness",
            "Maintain soil N-P-K nutrient balance and pH between 6.0 and 6.8",
            "Ensure adequate spacing (45-60 cm) for air circulation",
            "Perform regular crop scoutings to detect early signs of stress"
        ],
        "treatments": [
            "No chemical or therapeutic intervention needed.",
            "Maintain routine cultural hygiene and crop scouting schedules."
        ],
        "management": [
            "Continue preventative crop scouting and sanitation routines.",
            "Maintain balanced fertigation and avoid physical mechanical leaf damage during pruning.",
            "Consult local agricultural extension specialists for seasonal baseline maintenance protocols."
        ],
        "look_alikes": "Can occasionally be confused with asymptomatic early stages of viral infection or latent bacterial incubation before visual lesion onset."
    },

    "early_blight": {
        "id": "early_blight",
        "name": "Early Blight",
        "scientific_name": "Alternaria solani & Alternaria tomatophila (Fungi)",
        "category": "fungal",
        "category_label": "Fungal Disease",
        "ml_supported": True,
        "is_healthy": False,
        "severity": "Moderate to High (Defoliation & Sunscald Risk)",
        "badge_color": "warning",
        "description": "A prevalent fungal foliar disease targeting older, lower foliage first, characterized by circular brown-black lesions with concentric rings resembling a target board.",
        "symptoms": [
            "Dark brown to black necrotic spots with concentric target-board rings",
            "Yellow chlorotic halos surrounding lesions",
            "Progresses upwards from senescence-prone lower leaves",
            "Extensive leaf yellowing, wilting, collar rot on stems, and defoliation"
        ],
        "favorable_conditions": "Warm, humid conditions (24-29°C) combined with repeated wetting-drying cycles on leaf surfaces. Spores overwinter in infected plant debris.",
        "causes": "Warm, humid conditions (24-29°C) combined with repeated wetting-drying cycles on leaf surfaces. Spores overwinter in infected plant debris.",
        "prevention": [
            "Rotate crops with non-solanaceous plants for at least 2-3 years",
            "Mulch base of plants to prevent soil splashing onto bottom leaves",
            "Prune lowest 30 cm of branches to improve canopy air circulation",
            "Avoid overhead irrigation; water only at the soil line in early morning"
        ],
        "treatments": [
            "Remove and destroy severely affected foliage immediately; do not compost.",
            "Apply copper-based protectants or bio-fungicide Bacillus subtilis upon early symptom detection.",
            "Consult local agricultural extension guidance for locally registered fungicides (e.g., chlorothalonil, azoxystrobin)."
        ],
        "management": [
            "Remove and safely destroy severely infected lower leaves; do not compost infected residues.",
            "Apply preventative protectant sprays when weather forecasts indicate prolonged leaf wetness.",
            "Consult local agricultural extension agents for certified fungicide choices and spray intervals appropriate for your region."
        ],
        "look_alikes": "Frequently confused with Target Spot (Corynespora cassiicola) and Septoria Leaf Spot. Target spot lesions are more randomly distributed throughout the canopy without strict lower-canopy initiation."
    },

    "late_blight": {
        "id": "late_blight",
        "name": "Late Blight",
        "scientific_name": "Phytophthora infestans (Oomycete)",
        "category": "fungal",
        "category_label": "Oomycete / Water Mold",
        "ml_supported": True,
        "is_healthy": False,
        "severity": "Critical (Potential Total Crop Loss in 7-14 Days)",
        "badge_color": "danger",
        "description": "A devastating, fast-moving water mold disease capable of destroying entire tomato crop stands within days during cool, damp, foggy weather.",
        "symptoms": [
            "Large, irregular water-soaked pale-green to dark brown or purplish-black lesions",
            "Delicate white velvety fungal/spore growth on leaf undersides in high humidity",
            "Dark brown greasy lesions on stems and petiole collapse",
            "Firm, rough, greasy brown decay on fruit surfaces"
        ],
        "favorable_conditions": "Cool, wet conditions (15–22°C) with relative humidity above 90% favor late blight development. Windborne sporangia can travel long distances during cloudy or rainy weather, spreading the pathogen from infected plants to healthy ones.",
        "causes": "Cool, wet conditions (15–22°C) with relative humidity above 90% favor late blight development. Windborne sporangia can travel long distances during cloudy or rainy weather, spreading the pathogen from infected plants to healthy ones.",
        "prevention": [
            "Plant resistant tomato cultivars (e.g., Mountain Magic, Defiant PhR)",
            "Avoid planting adjacent to potato fields or volunteer nightshades",
            "Ensure wide plant spacing and plant in full sun to accelerate foliage drying",
            "Monitor regional agricultural extension disease alert bulletins"
        ],
        "treatments": [
            "Act immediately upon detection: rogue and bag infected plants completely.",
            "Apply preventative copper fungicides before humid rainy spells.",
            "Utilize systemic targeted fungicides under registered agronomist guidance."
        ],
        "management": [
            "Rogue and bag severely diseased plants immediately to protect surrounding acreage.",
            "Apply approved preventative protective fungicides prior to rainfall events when disease advisories trigger in the district.",
            "Always consult regional agricultural university extension guidelines for legally registered oomycete treatments."
        ],
        "look_alikes": "Can resemble severe physical frost injury or rapid Botrytis gray mold collapse. White sporulation on the underside in humid mornings confirms late blight."
    },

    "leaf_mold": {
        "id": "leaf_mold",
        "name": "Leaf Mold",
        "scientific_name": "Passalora fulva / Cladosporium fulvum (Fungus)",
        "category": "fungal",
        "category_label": "Fungal Disease",
        "ml_supported": True,
        "is_healthy": False,
        "severity": "Moderate (High in High-Tunnel / Greenhouse Cultivation)",
        "badge_color": "info",
        "description": "Common foliage disease predominantly occurring in high-humidity protected environments such as greenhouses, polyhouses, or densely planted garden plots.",
        "symptoms": [
            "Pale green to yellowish indistinct chlorotic patches on upper leaf surface",
            "Olive-green to brownish velvety mold growth on corresponding lower surface",
            "Leaves curl, wither, and drop prematurely without circular target spots",
            "Progresses upwards from older leaves; fruits rarely infected directly"
        ],
        "favorable_conditions": "High relative humidity (>85%) and moderate temperatures (21-24°C) with stagnant ventilation inside protected structures.",
        "causes": "High relative humidity (>85%) and moderate temperatures (21-24°C) with poor ventilation in protected cultivation structures.",
        "prevention": [
            "Increase greenhouse airflow using exhaust fans and horizontal circulation",
            "Drip irrigate early in the day so soil surface dries before nightfall",
            "Maintain heating or ventilation to prevent condensation on foliage",
            "Select leaf-mold resistant hybrid varieties (Cf resistance genes)"
        ],
        "treatments": [
            "Prune lower canopy leaves to facilitate air movement throughout rows.",
            "Spray sulfur or copper fungicides thoroughly covering undersides of foliage.",
            "Apply bio-protective sprays like Trichoderma harzianum or potassium bicarbonate."
        ],
        "management": [
            "Increase greenhouse ventilation and horizontal fans to keep foliage dry.",
            "Prune lower canopy foliage to facilitate laminar airflow through dense rows.",
            "Seek guidance from agricultural extension services for greenhouse-registered biofungicides."
        ],
        "look_alikes": "May be confused with Powdery Mildew (which produces white powdery mycelium on the upper leaf surface) or early Spider Mite stippling."
    },

    "septoria_leaf_spot": {
        "id": "septoria_leaf_spot",
        "name": "Septoria Leaf Spot",
        "scientific_name": "Septoria lycopersici (Fungus)",
        "category": "fungal",
        "category_label": "Fungal Disease",
        "ml_supported": True,
        "is_healthy": False,
        "severity": "Moderate to High (Premature Defoliation & Sunscald)",
        "badge_color": "secondary",
        "description": "A very common fungal pathogen causing numerous tiny circular spots with grey-white centers and dark brown margins across leaves.",
        "symptoms": [
            "Dozens of small circular spots (2-3 mm) with light tan/grey centers and dark margins",
            "Tiny black specks (pycnidia fruiting bodies) visible inside spot centers with magnification",
            "Progresses rapidly from bottom leaves upward, causing heavy yellowing and leaf loss",
            "Fruits remain unaffected directly, but exposed to sunscald due to defoliation"
        ],
        "favorable_conditions": "Warm temperatures (20-25°C) combined with prolonged rainfall, high humidity, or overhead splashing water.",
        "causes": "Fungus thrives in warm (20-25°C) and wet weather, spread by water splashes, tools, hands, and insects from infested debris.",
        "prevention": [
            "Deep mulch around plants immediately after transplanting",
            "Disinfect pruning shears between plants with 70% alcohol or 10% bleach",
            "Clean up all fallen leaves and garden debris at season end",
            "Do not work in tomato patch while foliage is wet from rain or dew"
        ],
        "treatments": [
            "Prune infected bottom leaves at the earliest sign of spotting.",
            "Apply preventative copper hydroxide or biofungicides weekly during damp weather.",
            "In severe cases, spray chlorothalonil or mancozeb according to package instructions."
        ],
        "management": [
            "Prune and destroy infected lower leaves at first notice before pycnidia disperse spores.",
            "Install drip irrigation and organic mulch to suppress soil splash transmission.",
            "Consult local extension officers for approved organic copper or synthetic protective options."
        ],
        "look_alikes": "Frequently confused with Bacterial Speck and Bacterial Spot. Septoria spots are distinguished by their distinct grey/white sunken centers with black pycnidial dots."
    },

    "bacterial_spot": {
        "id": "bacterial_spot",
        "name": "Bacterial Spot",
        "scientific_name": "Xanthomonas species complex (X. perforans, X. vesicatoria, X. gardneri)",
        "category": "bacterial",
        "category_label": "Bacterial Disease",
        "ml_supported": False,
        "is_healthy": False,
        "severity": "High (Severe Leaf Drop & Market Unsalable Fruit)",
        "badge_color": "danger",
        "description": "A widespread seedborne and wind-driven bacterial infection causing small, water-soaked, dark lesions on leaves, stems, and rough raised scabs on fruit.",
        "symptoms": [
            "Small (1-3 mm), dark brown to black, water-soaked, angular circular spots",
            "Lesions often surrounded by yellow chlorotic halos in humid conditions",
            "Spot centers may tear or drop out, creating a ragged shot-hole appearance",
            "Extensive blighting of leaf margins and premature foliage drop",
            "Raised, blister-like brown scabs with cracked margins on developing green fruit"
        ],
        "favorable_conditions": "Warm, wet weather (25-30°C) and prolonged leaf wetness caused by driving rain, high humidity (>80%), or overhead sprinkler irrigation.",
        "causes": "Xanthomonas bacterial species surviving in contaminated seed, volunteer nightshades, or infected crop residue.",
        "prevention": [
            "Use certified pathogen-free seeds or hot-water-treated seed stocks",
            "Rotate crops for at least 2 years away from solanaceous plants (peppers, tomatoes)",
            "Strictly avoid overhead irrigation; irrigate solely through ground drip lines",
            "Never cultivate, tie, or prune plants while the canopy is wet"
        ],
        "treatments": [
            "Sanitize trellising stakes and tools with 10% bleach or sanitizing quaternary solution.",
            "Apply preventative copper bactericide combined with mancozeb as recommended by local extension.",
            "Consult extension experts regarding bio-control bacteriophages or Actigard systemic plant inducers."
        ],
        "management": [
            "Use clean, tested seed and transplants, and discard symptomatic nursery trays immediately.",
            "Avoid overhead irrigation, remove infected plant debris, and sanitize trellising stakes.",
            "Follow locally recommended disease management guidance, noting that copper tolerance is prevalent in certain districts."
        ],
        "look_alikes": "Very similar to Bacterial Speck (Pseudomonas syringae) and Septoria Leaf Spot. Bacterial speck spots are typically smaller, and Septoria spots exhibit lighter grey centers with black fungal fruiting bodies."
    },

    "target_spot": {
        "id": "target_spot",
        "name": "Target Spot",
        "scientific_name": "Corynespora cassiicola (Fungus)",
        "category": "fungal",
        "category_label": "Fungal Disease",
        "ml_supported": False,
        "is_healthy": False,
        "severity": "Moderate to High (Extensive Canopy Blight)",
        "badge_color": "warning",
        "description": "A destructive fungal foliar disease that causes necrotic lesions throughout the canopy, often characterized by concentric light brown and dark brown rings.",
        "symptoms": [
            "Brown lesions with concentric rings, sometimes surrounded by yellow tissue halos",
            "Lesions enlarge (5-10 mm), coalesce, and cause extensive defoliation",
            "Appears across upper and middle canopy as well as lower leaves",
            "Deeply sunken, brown crater-like lesions on green or ripe fruits"
        ],
        "favorable_conditions": "Warm temperatures (20-28°C), high humidity, and prolonged leaf wetness or heavy morning dew.",
        "causes": "Corynespora cassiicola fungal spores spread via wind, splashing water, and machinery.",
        "prevention": [
            "Improve airflow through proper row orientation, wide spacing, and regular staking",
            "Avoid prolonged leaf wetness and avoid working among damp crops",
            "Remove weeds and alternate host species (e.g., cucumber, soybean, cotton) near tomato plots",
            "Destroy and bury crop debris promptly after harvest"
        ],
        "treatments": [
            "Prune infected branches to limit spore production inside the canopy.",
            "Apply preventative protectant fungicides according to local agricultural university spray schedules.",
            "Rotate fungicide chemical classes to prevent resistance development."
        ],
        "management": [
            "Improve canopy airflow and avoid prolonged leaf wetness.",
            "Remove infected debris and seek local agricultural extension advice for registered fungicide options.",
            "Rotate chemical modes of action (FRAC codes) to suppress fungicide resistance."
        ],
        "look_alikes": "Strongly resembles Early Blight (Alternaria solani). However, Target Spot lesions appear throughout the canopy and often feature a more ragged, pale center."
    },

    "tomato_mosaic_virus": {
        "id": "tomato_mosaic_virus",
        "name": "Tomato Mosaic Virus (ToMV)",
        "scientific_name": "Tomato mosaic virus (ToMV / Tobamovirus)",
        "category": "viral",
        "category_label": "Viral Disease",
        "ml_supported": False,
        "is_healthy": False,
        "severity": "High (Permanent Stunting & Internal Fruit Necrosis)",
        "badge_color": "danger",
        "description": "A highly stable, mechanically transmitted viral pathogen that causes characteristic mottled patterns, distortion, and significant yield loss.",
        "symptoms": [
            "Alternating light and dark green mosaic patterns across leaf blades",
            "Leaf distortion, leaf curling, reduced leaf size ('shoestringing' or fern-like appearance)",
            "Stunted plant growth and reduced vegetative vigor",
            "Fruit may display uneven ripening, internal brown necrosis, and yellowish blotches"
        ],
        "favorable_conditions": "Spread mechanically through contaminated hands, tools, plant material, clothing, and infected seed stocks. Virus remains infectious in dry debris for years.",
        "causes": "Tobamovirus transmission via contaminated seeds, hands, pruning shears, and sap contact.",
        "prevention": [
            "Use certified clean seed stocks and plant ToMV-resistant tomato varieties (e.g., Tm-2^2 resistance gene)",
            "Sanitize tools and pruning shears between plants in 10% bleach or non-fat milk solution",
            "Wash hands thoroughly with soap or milk solution before handling plants",
            "Avoid handling healthy plants after touching suspect or infected ones"
        ],
        "treatments": [
            "There is no chemical cure for viral infections once established.",
            "Rogue and safely destroy infected plants appropriately; do not compost.",
            "Strictly avoid handling healthy plants after touching suspect infected foliage."
        ],
        "management": [
            "Use certified clean seed and resistant cultivars.",
            "Sanitize tools, stakes, and hands, and remove infected plants appropriately (burn or bag).",
            "Avoid handling healthy plants after touching infected ones, and prohibit smoking/tobacco near crops."
        ],
        "look_alikes": "Can be easily confused with Tobacco Mosaic Virus (TMV), Cucumber Mosaic Virus (CMV), or sub-lethal phenoxy herbicide drift (e.g., 2,4-D)."
    },

    "yellow_leaf_curl_virus": {
        "id": "yellow_leaf_curl_virus",
        "name": "Tomato Yellow Leaf Curl Disease (TYLCD)",
        "scientific_name": "Tomato yellow leaf curl virus complex (TYLCV / Begomovirus)",
        "category": "viral",
        "category_label": "Viral Disease",
        "ml_supported": False,
        "is_healthy": False,
        "severity": "Critical (Severe Floral Abscission & Complete Stunting)",
        "badge_color": "danger",
        "description": "A devastating viral disease transmitted by the silverleaf whitefly (Bemisia tabaci) that causes upward cupping, severe chlorosis, and vegetative dwarfism.",
        "symptoms": [
            "Upward curling of leaf margins into a spoon-like shape",
            "Prominent interveinal yellowing (chlorosis), especially on younger leaves",
            "Marked reduction in leaflet size and leaf area",
            "Severe plant stunting, erect bushy architecture, and heavy flower abortion",
            "Dramatically reduced fruit set; flowers drop prematurely before pollination"
        ],
        "favorable_conditions": "Warm climates and long dry spells that favor whitefly vector breeding, movement, and regional migration.",
        "causes": "Begomovirus transmitted persistently by the sweetpotato/silverleaf whitefly vector (Bemisia tabaci).",
        "prevention": [
            "Use suitable resistant hybrid varieties (bearing Ty-1, Ty-3, or Ty-5 resistance genes)",
            "Install 50-mesh insect netting in greenhouses and nurseries to exclude whiteflies",
            "Use reflective silver or aluminized mulches to repel incoming whiteflies",
            "Manage weeds around plots that can serve as alternative viral or vector reservoirs"
        ],
        "treatments": [
            "No chemical cure exists for infected plants; infected specimens must be removed.",
            "Manage whitefly vectors with approved insecticidal soaps, horticultural oils, or bio-insecticides like Beauveria bassiana.",
            "Consult local agricultural extension advisory for integrated pest management (IPM) whitefly protocols."
        ],
        "management": [
            "Use suitable resistant varieties and certified transplants.",
            "Monitor whitefly populations with yellow sticky cards and manage weeds systematically.",
            "Follow local integrated pest management (IPM) guidance, and immediately rogue infected plants to prevent field spread."
        ],
        "look_alikes": "Can be confused with physiological leaf roll, severe phosphorus deficiency, or early herbicide exposure. TYLCV is distinguished by pronounced yellowing accompanied by leaf size reduction and flower drop."
    },

    "bacterial_speck": {
        "id": "bacterial_speck",
        "name": "Bacterial Speck",
        "scientific_name": "Pseudomonas syringae pv. tomato (Bacteria)",
        "category": "bacterial",
        "category_label": "Bacterial Disease",
        "ml_supported": False,
        "is_healthy": False,
        "severity": "Moderate to High in Cool Wet Seasons",
        "badge_color": "danger",
        "description": "A bacterial disease causing numerous tiny, dark brown to black punctate specks surrounded by prominent yellow chlorotic halos, thriving in cool wet conditions.",
        "symptoms": [
            "Tiny (under 1-2 mm) dark brown to black spots, often with narrow yellow halos",
            "Fruit may also develop small, superficial, dark brown spots surrounded by green halos",
            "Lesions may coalesce along leaf tips and margins, causing leaf distortion and curling",
            "Stems and floral pedicels may also develop elongated dark specks"
        ],
        "favorable_conditions": "Cool to moderate, wet weather (13-24°C) with frequent rain, driving wind, or prolonged leaf wetness.",
        "causes": "Pseudomonas syringae pathovars surviving in seeds, weed hosts, and plant residue.",
        "prevention": [
            "Use healthy, certified disease-free seed and transplants",
            "Avoid working among wet plants and avoid pruning during damp mornings",
            "Sanitize pruning shears, stakes, and transplant flats",
            "Remove and incorporate infected crop debris immediately after harvest"
        ],
        "treatments": [
            "Apply preventative copper hydroxide bactericide combined with mancozeb upon regional disease warnings.",
            "Disinfect stakes and pruning tools between garden blocks.",
            "Consult local agricultural extension for resistance-monitoring reports."
        ],
        "management": [
            "Use healthy seed and transplants, and rotate away from solanaceous crops for 2 years.",
            "Avoid working among wet plants to prevent mechanical bacterial transmission.",
            "Sanitize tools, remove infected debris, and consult local extension guidance for copper bactericide programs."
        ],
        "look_alikes": "Frequently confused with Bacterial Spot (Xanthomonas) and Septoria Leaf Spot. Bacterial speck lesions are smaller (pinpoint specks) and prefer cooler weather than Bacterial Spot."
    },

    "powdery_mildew": {
        "id": "powdery_mildew",
        "name": "Powdery Mildew",
        "scientific_name": "Oidium neolycopersici & Leveillula taurica (Fungi)",
        "category": "fungal",
        "category_label": "Fungal Disease",
        "ml_supported": False,
        "is_healthy": False,
        "severity": "Moderate (Yield Depletion Through Premature Senescence)",
        "badge_color": "info",
        "description": "A prevalent fungal foliar disease resulting in talcum-powder-like white fungal colonies on upper leaf surfaces or internal chlorotic patches.",
        "symptoms": [
            "White powdery patches on leaf surfaces, expanding to cover large foliage areas",
            "Underlying leaf tissue turns pale green, then yellow, and eventually dries out",
            "Severe cases lead to complete leaf browning, withering, and premature defoliation",
            "Stems and sepals can also show light powdery fungal sporulation in heavy outbreaks"
        ],
        "favorable_conditions": "Favorable temperatures (18-26°C) and high local relative humidity. Unlike downy mildews, free water droplets are not always required for spore germination.",
        "causes": "Airborne conidia of obligate biotrophic powdery mildew fungal species.",
        "prevention": [
            "Improve airflow through pruning and generous plant spacing",
            "Monitor plants regularly for early white powdery colonies",
            "Avoid excessive nitrogen fertilization which produces overly lush, susceptible foliage",
            "Remove severely affected foliage where practical to reduce inoculum pressure"
        ],
        "treatments": [
            "Spray with potassium bicarbonate or horticultural oils at first notice of powdery spots.",
            "Apply elemental sulfur or bio-fungicide Bacillus amyloliquefaciens.",
            "Consult agricultural extension advisors for locally approved systemic fungicides."
        ],
        "management": [
            "Improve airflow and light penetration throughout the crop canopy.",
            "Monitor plants weekly and remove severely affected foliage where practical.",
            "Seek locally appropriate treatment advice, including registered bio-fungicides or sulfur compounds."
        ],
        "look_alikes": "Can be confused with Leaf Mold (which produces olive-brown mold primarily on the underside) or pesticide spray residues dried on the leaf blade."
    },

    "gray_leaf_spot": {
        "id": "gray_leaf_spot",
        "name": "Gray Leaf Spot",
        "scientific_name": "Stemphylium species (including S. solani, S. lycopersici)",
        "category": "fungal",
        "category_label": "Fungal Disease",
        "ml_supported": False,
        "is_healthy": False,
        "severity": "Moderate to Severe (Rapid Canopy Defoliation)",
        "badge_color": "warning",
        "description": "A fungal disease causing small, dark, circular lesions that rapidly develop glazed, grey-white centers that crack and tear, leading to heavy premature leaf shedding.",
        "symptoms": [
            "Small gray to brown lesions with darker margins on leaf blades",
            "Lesions enlarge, merge together, and cause extensive leaf yellowing and death",
            "Center of mature spots turns glazed, gray, and frequently cracks or drops out (shot-hole)",
            "Progresses upwards through the canopy, leaving stems bare while fruit remains uninfected"
        ],
        "favorable_conditions": "Warm, humid weather (24-28°C) and extended leaf wetness from rain, fog, or overhead watering.",
        "causes": "Stemphylium fungal spores surviving on solanaceous weeds (e.g., groundcherries, horsenettle) and crop debris.",
        "prevention": [
            "Improve ventilation and row orientation to accelerate drying",
            "Avoid overhead watering; irrigate at soil level",
            "Remove and destroy infected crop residues and volunteer weeds promptly",
            "Select resistant cultivars containing the Sm resistance gene"
        ],
        "treatments": [
            "Prune diseased lower leaves early in the season to slow upward transmission.",
            "Apply broad-spectrum protectant fungicides (chlorothalonil, mancozeb) as guided by local agricultural extension.",
            "Consult local authorities for organic copper spray protocols."
        ],
        "management": [
            "Improve canopy ventilation and avoid overhead watering.",
            "Remove infected crop residues promptly and manage alternate weed hosts.",
            "Use locally recommended management practices and consult extension agents for approved fungicides."
        ],
        "look_alikes": "Very similar to Septoria Leaf Spot and Bacterial Spot. Septoria spots have tiny black pycnidia specks inside the grey center, which are absent in Gray Leaf Spot."
    },

    "spider_mites": {
        "id": "spider_mites",
        "name": "Spider Mite Damage",
        "scientific_name": "Tetranychus urticae (Two-Spotted Spider Mite - Arachnida / Pest)",
        "category": "pest_related",
        "category_label": "Pest Damage (Not a Plant Disease)",
        "ml_supported": False,
        "is_healthy": False,
        "severity": "Moderate to High (Severe Foliage Desiccation)",
        "badge_color": "warning",
        "description": "Pest injury caused by minute arachnid mites feeding on the undersides of leaves, piercing individual plant cells and sucking out sap and chlorophyll.",
        "symptoms": [
            "Fine pale stippling (pinpoint yellow or white speckling) across the upper leaf surface",
            "Yellow or bronze discoloration as cell damage spreads across the leaflet",
            "Fine silken webbing across leaf undersides, petiole junctions, and shoot tips in heavier infestations",
            "Leaf drying, scorched papery texture, and premature leaf drop under continued feeding"
        ],
        "favorable_conditions": "Hot, dry conditions (>30°C and low humidity) often favor explosive spider mite population growth.",
        "causes": "Feeding by dense colonies of two-spotted spider mites on the abaxial (lower) leaf epidermis.",
        "prevention": [
            "Inspect leaf undersides regularly, especially during hot, dry weather periods",
            "Conserve beneficial predators (predatory mites, lady beetles, minute pirate bugs)",
            "Minimize dust along road borders which disrupts natural predators",
            "Avoid excessive synthetic pyrethroid sprays that eliminate beneficial predatory mites"
        ],
        "treatments": [
            "Wash foliage undersides with high-pressure water spray to knock down populations.",
            "Apply insecticidal soaps, neem oil, or horticultural oils ensuring complete coverage of leaf undersides.",
            "Consult extension experts regarding selective miticides (acaricides) registered in your area."
        ],
        "management": [
            "Inspect leaf undersides routinely with a 10x hand lens.",
            "Conserve beneficial predators and avoid disruptive broad-spectrum insecticides.",
            "Remove heavily infested plant material when practical and seek local integrated pest management (IPM) advice."
        ],
        "look_alikes": "Early stippling can resemble nutrient chlorosis, Thrips feeding damage, or early Leaf Mold yellowing. Silken webbing and microscopic visual inspection confirm mites."
    },

    "leaf_miner": {
        "id": "leaf_miner",
        "name": "Leaf Miner Damage",
        "scientific_name": "Liriomyza sativae & L. trifolii (Insecta / Agromyzidae)",
        "category": "pest_related",
        "category_label": "Pest Damage (Not a Plant Disease)",
        "ml_supported": False,
        "is_healthy": False,
        "severity": "Low to Moderate (Photosynthetic Impairment)",
        "badge_color": "info",
        "description": "Insect pest damage characterized by winding, serpentine tunnels created by fly larvae feeding internally within the leaf mesophyll tissue.",
        "symptoms": [
            "Winding, serpentine white to translucent trails or mines across leaf blades",
            "Dark frass (insect excrement) visible inside the winding leaf mine trails",
            "Small whitish feeding punctures (stipples) on leaf surface created by adult female flies",
            "Heavily mined leaves dry out, turn brown, and drop prematurely"
        ],
        "favorable_conditions": "Warm weather (20-30°C) with broad-spectrum pesticide misuse that eradicates natural parasitic wasps (Diglyphus isaea).",
        "causes": "Larval feeding inside leaf tissue by agromyzid leafminer flies.",
        "prevention": [
            "Use yellow sticky traps around crop perimeters to monitor and trap adult flies",
            "Conserve beneficial parasitic wasps (e.g., Diglyphus isaea, Dacnusa sibirica)",
            "Cover young seedlings in nurseries with floating row covers or insect netting",
            "Avoid prophylactic broad-spectrum insecticide sprays that kill natural parasitoids"
        ],
        "treatments": [
            "Hand-pick and destroy individual mined leaves when infestations are minimal.",
            "Apply neem oil or azadirachtin which acts as an insect growth regulator on young larvae.",
            "Consult local extension specialists for targeted, translaminar insecticides (e.g., spinosad)."
        ],
        "management": [
            "Inspect underside of mines for parasitoid exit holes before spraying, as natural biocontrol often suppresses miners.",
            "Apply translaminar insecticides only if larval density exceeds established university economic thresholds.",
            "Consult agricultural extension advisors for regional resistance management."
        ],
        "look_alikes": "The serpentine winding tunnels are unmistakable and rarely confused with fungal or bacterial pathogens."
    },

    "nutrient_deficiency": {
        "id": "nutrient_deficiency",
        "name": "Nutrient Deficiency / Nutrient Stress",
        "scientific_name": "Abiotic / Physiological Stress (N, P, K, Mg, Fe imbalance)",
        "category": "physiological",
        "category_label": "Physiological Condition",
        "ml_supported": False,
        "is_healthy": False,
        "severity": "Variable (Impairs Root, Canopy, and Yield Development)",
        "badge_color": "secondary",
        "description": "Non-pathogenic, abiotic physiological disorders caused by insufficient availability, root uptake failure, or soil pH lockup of vital plant macro/micronutrients.",
        "symptoms": [
            "Nitrogen (N) Deficiency: Uniform pale green to yellowing starting on oldest lower foliage, accompanied by slow growth",
            "Potassium (K) Deficiency: Marginal leaf chlorosis and necrosis (edge scorch) on mature leaves",
            "Magnesium (Mg) Deficiency: Striking interveinal chlorosis on older leaves while veins remain green, often progressing to purple-brown tinting",
            "Iron (Fe) Deficiency: Bright yellow interveinal chlorosis appearing exclusively on the youngest apical shoots",
            "Phosphorus (P) Deficiency: Dark green leaves with distinct purplish-bronze tinting on leaf undersides and veins"
        ],
        "favorable_conditions": "Improper soil pH (<5.5 or >7.5), over-watering, compacted soil, drought, root nematode damage, or unbalanced fertilizer application.",
        "causes": "Insufficient soil nutrient supply, cold soil temperatures restricting root uptake, or root zone pH lockup.",
        "prevention": [
            "Conduct routine soil or foliar tissue testing before each growing cycle",
            "Maintain soil pH between 6.2 and 6.8 to ensure optimal micronutrient availability",
            "Incorporate well-composted organic matter to improve cation exchange capacity (CEC)",
            "Follow balanced N-P-K fertigation schedules tailored to tomato growth stages"
        ],
        "treatments": [
            "Adjust irrigation to ensure roots are not waterlogged or suffering drought stress.",
            "Apply balanced soluble foliar fertilizers as a temporary remedy.",
            "Consult agricultural extension soil testing laboratories for precise amendment recommendations."
        ],
        "management": [
            "Perform a certified laboratory soil and leaf tissue test before applying heavy single-element fertilizers.",
            "Check root health to confirm whether the issue is true soil deficiency or root pathogen impairment.",
            "Seek guidance from agricultural extension specialists for precise fertigation adjustments."
        ],
        "look_alikes": "Frequently confused with viral infections (e.g., Mosaic Virus or TYLCV) and early root rot. Nutrient deficiencies typically follow bilateral symmetry across the plant canopy, whereas viral and pathogen infections are often localized or random."
    },

    "unknown_uncertain": {
        "id": "unknown_uncertain",
        "name": "Unknown or Uncertain Leaf Condition",
        "scientific_name": "Atypical / Mixed Etiology / Undetermined",
        "category": "uncertain",
        "category_label": "Uncertain / Unverified",
        "ml_supported": False,
        "is_healthy": False,
        "severity": "Unspecified (Requires Physical Agronomic Inspection)",
        "badge_color": "dark",
        "description": "Visual symptoms that are ambiguous, masked by multiple concurrent stresses (e.g., blight with nutrient deficiency), or physical abiotic damage like sunscald, mechanical injury, or chemical burn.",
        "symptoms": [
            "Atypical discoloration, irregular tears, chemical burn margins, or ambiguous lesions",
            "Overlapping symptoms from multiple potential diseases or pest interactions",
            "Non-distinct necrotic patches lacking hallmark diagnostic signs (e.g., no target rings, no spores, no pycnidia)",
            "Damage caused by hail, pesticide burn, fertilizer salt scorch, or heat stress"
        ],
        "favorable_conditions": "Extreme weather events, herbicide drift, variable microclimates, or multi-pest infestations.",
        "causes": "Complex abiotic injury, poly-microbial co-infections, or photographic distortion.",
        "prevention": [
            "Maintain consistent record-keeping of spray dates, fertilizer applications, and weather events",
            "Protect crops from mechanical damage and windborne chemical drift",
            "Inspect both upper and lower canopy leaves across multiple plants"
        ],
        "treatments": [
            "Do not apply speculative chemical treatments without a definitive diagnosis.",
            "Isolate affected specimens if contagious pathology is suspected.",
            "Collect a fresh physical leaf sample and submit it to a university plant pathology diagnostic clinic."
        ],
        "management": [
            "Do not spray broad-spectrum chemicals on unverified leaf conditions, as this may worsen plant stress.",
            "Take multiple high-resolution photos of both upper and lower leaf surfaces in diffused natural light.",
            "Consult your nearest local university or county agricultural extension office for professional laboratory culturing or PCR testing."
        ],
        "look_alikes": "Can mimic multiple genuine pathogens, herbicide drift, or physical hail injury."
    }
}

# The 5 classes actively supported by the ML inference pipeline
MODEL_CLASSES = [
    "Healthy",
    "Early blight",
    "Late blight",
    "Leaf mold",
    "Septoria leaf spot"
]
CLASS_NAMES = MODEL_CLASSES
MODEL_SUPPORTED_CLASSES = MODEL_CLASSES

# Machine-readable IDs
ALL_CATEGORY_IDS = list(DISEASE_CATALOG.keys())

def get_disease_info(query):
    """
    Retrieve full informational dictionary for a predicted class name or ID.
    Performs case-insensitive matching across ID, name, and aliases.
    """
    if not query:
        return DISEASE_CATALOG["unknown_uncertain"]

    query_clean = str(query).strip().lower().replace("_", " ").replace("-", " ")
    
    # 1. Exact or normalized ID match
    for cat_id, data in DISEASE_CATALOG.items():
        id_norm = cat_id.replace("_", " ")
        if query_clean == id_norm or query_clean == cat_id:
            return data
            
    # 2. Match against display name
    for cat_id, data in DISEASE_CATALOG.items():
        name_norm = data["name"].lower().replace("-", " ")
        if query_clean == name_norm or query_clean in name_norm or name_norm in query_clean:
            return data

    # 3. Partial keyword matching
    keywords_map = {
        "healthy": "healthy",
        "early": "early_blight",
        "late": "late_blight",
        "mold": "leaf_mold",
        "septoria": "septoria_leaf_spot",
        "bacterial spot": "bacterial_spot",
        "bacterial speck": "bacterial_speck",
        "target": "target_spot",
        "mosaic": "tomato_mosaic_virus",
        "curl": "yellow_leaf_curl_virus",
        "tylcd": "yellow_leaf_curl_virus",
        "tylcv": "yellow_leaf_curl_virus",
        "mite": "spider_mites",
        "spider": "spider_mites",
        "powdery": "powdery_mildew",
        "gray": "gray_leaf_spot",
        "grey": "gray_leaf_spot",
        "miner": "leaf_miner",
        "deficiency": "nutrient_deficiency",
        "nutrient": "nutrient_deficiency",
        "uncertain": "unknown_uncertain",
        "unknown": "unknown_uncertain"
    }

    for kw, target_id in keywords_map.items():
        if kw in query_clean:
            return DISEASE_CATALOG[target_id]

    # Default fallback to uncertain
    return DISEASE_CATALOG["unknown_uncertain"]

def get_all_categories():
    """Returns list of all category dictionaries."""
    return list(DISEASE_CATALOG.values())

def get_categories_by_group(group_name=None):
    """
    Filter categories by biological category:
    'healthy', 'fungal', 'bacterial', 'viral', 'pest_related', 'physiological', 'uncertain'
    """
    if not group_name or group_name.lower() in ('all', ''):
        return get_all_categories()
    
    group_norm = group_name.strip().lower()
    return [
        cat for cat in DISEASE_CATALOG.values()
        if cat["category"] == group_norm
    ]

def get_ml_supported_categories():
    """Returns only the categories currently recognized by the ML model."""
    return [cat for cat in DISEASE_CATALOG.values() if cat.get("ml_supported", False)]

def get_reference_only_categories():
    """Returns categories documented in the encyclopedia but not yet supported by the ML model."""
    return [cat for cat in DISEASE_CATALOG.values() if not cat.get("ml_supported", False)]
