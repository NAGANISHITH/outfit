import cv2
import numpy as np
from PIL import Image

def detect_skin_type(image_path):
    """
    Detect skin type (dry, oily, normal, combination) from uploaded image
    """
    try:
        # Load image
        image = cv2.imread(image_path)
        if image is None:
            return "normal"
        
        # Convert to grayscale for texture analysis
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Calculate texture features
        # 1. Standard deviation (roughness indicator)
        std_dev = np.std(gray)
        
        # 2. Local binary pattern variance (texture measure)
        lbp_var = calculate_lbp_variance(gray)
        
        # 3. Brightness variance in different regions
        height, width = gray.shape
        regions = [
            gray[0:height//3, 0:width//3],  # Top-left
            gray[0:height//3, 2*width//3:width],  # Top-right
            gray[height//3:2*height//3, width//3:2*width//3],  # Center
            gray[2*height//3:height, 0:width//3],  # Bottom-left
            gray[2*height//3:height, 2*width//3:width]  # Bottom-right
        ]
        
        region_vars = [np.var(region) for region in regions]
        avg_region_var = np.mean(region_vars)
        
        # Classify based on texture features
        if std_dev < 25 and lbp_var < 50:
            return "dry"
        elif std_dev > 40 and lbp_var > 80:
            return "oily"
        elif avg_region_var > 100:
            return "combination"
        else:
            return "normal"
            
    except Exception as e:
        print(f"Skin type detection error: {e}")
        return "normal"

def calculate_lbp_variance(image):
    """
    Calculate Local Binary Pattern variance for texture analysis
    """
    try:
        # Simple LBP implementation
        rows, cols = image.shape
        lbp = np.zeros((rows-2, cols-2), dtype=np.uint8)
        
        for i in range(1, rows-1):
            for j in range(1, cols-1):
                center = image[i, j]
                code = 0
                
                # 8-neighbor LBP
                neighbors = [
                    image[i-1, j-1], image[i-1, j], image[i-1, j+1],
                    image[i, j+1], image[i+1, j+1], image[i+1, j],
                    image[i+1, j-1], image[i, j-1]
                ]
                
                for k, neighbor in enumerate(neighbors):
                    if neighbor >= center:
                        code += 2**k
                
                lbp[i-1, j-1] = code
        
        return np.var(lbp)
        
    except Exception as e:
        print(f"LBP calculation error: {e}")
        return 50

def get_skincare_tips(skin_type):
    """
    Get skincare tips based on detected skin type
    """
    tips = {
        "dry": [
            "Use a gentle, hydrating cleanser",
            "Apply moisturizer twice daily",
            "Use products with hyaluronic acid",
            "Avoid over-exfoliation"
        ],
        "oily": [
            "Use oil-free, non-comedogenic products",
            "Cleanse twice daily with salicylic acid",
            "Use lightweight, gel-based moisturizers",
            "Include niacinamide in your routine"
        ],
        "normal": [
            "Maintain a consistent skincare routine",
            "Use SPF daily",
            "Gentle exfoliation 2-3 times per week",
            "Keep skin hydrated"
        ],
        "combination": [
            "Use different products for T-zone and cheeks",
            "Gentle cleansing is key",
            "Use targeted treatments",
            "Balance oil control with hydration"
        ]
    }
    
    return tips.get(skin_type, tips["normal"])