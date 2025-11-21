# # import cv2
# # import numpy as np
# # from PIL import Image
# # import colorsys

# # def detect_skin_tone(image_path):
# #     """
# #     Detect skin tone from uploaded image using improved color analysis
# #     """
# #     try:
# #         # Load image
# #         image = cv2.imread(image_path)
# #         if image is None:
# #             print(f"Could not load image: {image_path}")
# #             return "Medium Warm"
        
# #         # Convert BGR to RGB
# #         image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
# #         # Resize image for faster processing
# #         height, width = image_rgb.shape[:2]
# #         if width > 500:
# #             scale = 500 / width
# #             new_width = int(width * scale)
# #             new_height = int(height * scale)
# #             image_rgb = cv2.resize(image_rgb, (new_width, new_height))
        
# #         # Convert to HSV for better skin detection
# #         hsv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)
        
# #         # Improved skin color detection with multiple ranges
# #         # Range 1: Light skin
# #         lower_skin1 = np.array([0, 20, 70], dtype=np.uint8)
# #         upper_skin1 = np.array([20, 255, 255], dtype=np.uint8)
        
# #         # Range 2: Medium skin
# #         lower_skin2 = np.array([0, 10, 60], dtype=np.uint8)
# #         upper_skin2 = np.array([25, 150, 200], dtype=np.uint8)
        
# #         # Range 3: Dark skin
# #         lower_skin3 = np.array([0, 30, 30], dtype=np.uint8)
# #         upper_skin3 = np.array([30, 255, 150], dtype=np.uint8)
        
# #         # Create masks
# #         mask1 = cv2.inRange(hsv, lower_skin1, upper_skin1)
# #         mask2 = cv2.inRange(hsv, lower_skin2, upper_skin2)
# #         mask3 = cv2.inRange(hsv, lower_skin3, upper_skin3)
        
# #         # Combine masks
# #         mask = cv2.bitwise_or(mask1, mask2)
# #         mask = cv2.bitwise_or(mask, mask3)
        
# #         # Apply morphological operations to clean up mask
# #         kernel = np.ones((3, 3), np.uint8)
# #         mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
# #         mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        
# #         # Extract skin pixels
# #         skin_pixels = image_rgb[mask > 0]
        
# #         if len(skin_pixels) == 0:
# #             print("No skin pixels detected, using fallback")
# #             # Fallback: analyze center region of image
# #             center_y, center_x = image_rgb.shape[0]//2, image_rgb.shape[1]//2
# #             region_size = min(50, center_y, center_x)
# #             center_region = image_rgb[center_y-region_size:center_y+region_size, 
# #                                     center_x-region_size:center_x+region_size]
# #             skin_pixels = center_region.reshape(-1, 3)
        
# #         # Calculate average skin color
# #         avg_color = np.mean(skin_pixels, axis=0)
# #         r, g, b = avg_color
        
# #         print(f"Average RGB: R={r:.1f}, G={g:.1f}, B={b:.1f}")
        
# #         # Convert to HSV for better analysis
# #         h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        
# #         # Calculate brightness and warmth indicators
# #         brightness = v  # Value component represents brightness
# #         warmth = (r - b) / 255  # Red minus blue indicates warmth
        
# #         # Additional analysis
# #         yellow_component = min(r, g) / 255  # Yellow undertones
# #         pink_component = (r - g) / 255 if r > g else 0  # Pink undertones
        
# #         print(f"Brightness: {brightness:.3f}, Warmth: {warmth:.3f}")
# #         print(f"Yellow component: {yellow_component:.3f}, Pink component: {pink_component:.3f}")
        
# #         # Enhanced classification logic
# #         if brightness < 0.35:  # Dark skin
# #             if warmth > 0.08 or yellow_component > 0.25:
# #                 return "Deep Warm"
# #             else:
# #                 return "Deep Cool"
# #         elif brightness < 0.65:  # Medium skin
# #             if warmth > 0.05 or yellow_component > 0.20:
# #                 return "Medium Warm"
# #             else:
# #                 return "Medium Cool"
# #         else:  # Light skin
# #             if warmth > 0.02 or yellow_component > 0.15:
# #                 return "Light Warm"
# #             else:
# #                 return "Light Cool"
                
# #     except Exception as e:
# #         print(f"Skin tone detection error: {e}")
# #         return "Medium Warm"  # Safe fallback

# # def get_complementary_colors(skin_tone):
# #     """
# #     Get complementary colors based on skin tone
# #     """
# #     color_palettes = {
# #         "Light Cool": ["#E6F3FF", "#B3D9FF", "#80BFFF", "#4D9FFF"],
# #         "Light Warm": ["#FFF2E6", "#FFE0B3", "#FFCC80", "#FFB84D"],
# #         "Medium Cool": ["#E0E6FF", "#C2D1FF", "#A3BCFF", "#85A7FF"],
# #         "Medium Warm": ["#FFE8D6", "#FFD1AD", "#FFBA85", "#FFA35C"],
# #         "Deep Cool": ["#D4EDDA", "#A8D8B8", "#7BC396", "#4FAE74"],
# #         "Deep Warm": ["#F8D7DA", "#F1AFB5", "#EA8790", "#E35F6B"]
# #     }
    
# #     return color_palettes.get(skin_tone, ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4"])

# # def analyze_skin_undertones(r, g, b):
# #     """
# #     Analyze skin undertones more precisely
# #     """
# #     # Convert to different color spaces for analysis
# #     lab_l = 0.2126 * r + 0.7152 * g + 0.0722 * b
    
# #     # Calculate color temperature
# #     color_temp = (r + g) / (2 * b) if b > 0 else 1
    
# #     # Determine undertones
# #     if color_temp > 1.1:
# #         return "warm"
# #     elif color_temp < 0.9:
# #         return "cool"
# #     else:
# #         return "neutral"




# import cv2
# import numpy as np
# import colorsys
# import os

# CASCADE_PATH = os.path.join(os.path.dirname(__file__), "haarcascade_frontalface_default.xml")

# def detect_skin_tone(image_path):
#     """
#     Detect skin tone using:
#     ✔ Face-only detection (forehead + cheeks)
#     ✔ Skin masking (3-range HSV)
#     ✔ Old advanced tone classification logic
#     """

#     try:
#         # Load image
#         image = cv2.imread(image_path)
#         if image is None:
#             print("Could not load image")
#             return "Medium Warm", (0, 0, 0), get_complementary_colors("Medium Warm")

#         # Convert to grayscale for face detection
#         gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#         # Load Haar face detector
#         face_cascade = cv2.CascadeClassifier(CASCADE_PATH)

#         # Detect faces
#         faces = face_cascade.detectMultiScale(gray, 1.1, 6)

#         if len(faces) == 0:
#             print("No face detected! Using fallback tone.")
#             return "Medium Warm", (0, 0, 0), get_complementary_colors("Medium Warm")

#         # Take largest detected face
#         x, y, w, h = max(faces, key=lambda f: f[2] * f[3])

#         # Face ROI: take upper half (forehead + cheeks)
#         face_roi = image[y:y + h // 2, x:x + w]

#         # Convert ROI to HSV
#         hsv = cv2.cvtColor(face_roi, cv2.COLOR_BGR2HSV)

#         # Three improved skin color ranges
#         lower1 = np.array([0, 20, 70], dtype=np.uint8)
#         upper1 = np.array([20, 255, 255], dtype=np.uint8)

#         lower2 = np.array([0, 10, 60], dtype=np.uint8)
#         upper2 = np.array([25, 150, 200], dtype=np.uint8)

#         lower3 = np.array([0, 30, 30], dtype=np.uint8)
#         upper3 = np.array([30, 255, 150], dtype=np.uint8)

#         # Create masks
#         mask1 = cv2.inRange(hsv, lower1, upper1)
#         mask2 = cv2.inRange(hsv, lower2, upper2)
#         mask3 = cv2.inRange(hsv, lower3, upper3)

#         mask = cv2.bitwise_or(mask1, mask2)
#         mask = cv2.bitwise_or(mask, mask3)

#         # Clean mask
#         kernel = np.ones((3, 3), np.uint8)
#         mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
#         mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

#         # Extract skin pixels
#         skin_pixels = face_roi[mask > 0]

#         # Fallback if no skin pixels
#         if len(skin_pixels) == 0:
#             print("No skin pixels found, using fallback region")
#             center_y, center_x = face_roi.shape[0] // 2, face_roi.shape[1] // 2
#             region = face_roi[center_y-30:center_y+30, center_x-30:center_x+30]
#             skin_pixels = region.reshape(-1, 3)

#         # Average skin color
#         avg = np.mean(skin_pixels, axis=0)
#         b, g, r = avg  # BGR → RGB

#         print(f"Average RGB: R={r:.1f}, G={g:.1f}, B={b:.1f}")

#         # Convert to HSV for tone analysis
#         h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)

#         brightness = v  # overall brightness
#         warmth = (r - b) / 255  # warm vs cool
#         yellow_comp = min(r, g) / 255  # yellow undertone
#         pink_comp = (r - g) / 255 if r > g else 0

#         print(f"Brightness: {brightness:.3f}, Warmth: {warmth:.3f}")
#         print(f"Yellow component: {yellow_comp:.3f}, Pink component: {pink_comp:.3f}")

#         # --- FINAL SKIN TONE CLASSIFICATION (old logic retained) ---
#         if brightness < 0.35:       # Deep
#             if warmth > 0.08 or yellow_comp > 0.25:
#                 tone = "Deep Warm"
#             else:
#                 tone = "Deep Cool"

#         elif brightness < 0.65:     # Medium
#             if warmth > 0.05 or yellow_comp > 0.20:
#                 tone = "Medium Warm"
#             else:
#                 tone = "Medium Cool"

#         else:                       # Light
#             if warmth > 0.02 or yellow_comp > 0.15:
#                 tone = "Light Warm"
#             else:
#                 tone = "Light Cool"

#         # Get complementary palette
#         palette = get_complementary_colors(tone)

#         return tone

#     except Exception as e:
#         print("Skin tone detection error:", e)
#         return "Medium Warm"


# def get_complementary_colors(skin_tone):
#     """
#     Get complementary shades for each skin tone.
#     """

#     color_palettes = {
#         "Light Cool":  ["#E6F3FF", "#B3D9FF", "#80BFFF", "#4D9FFF"],
#         "Light Warm":  ["#FFF2E6", "#FFE0B3", "#FFCC80", "#FFB84D"],
#         "Medium Cool": ["#E0E6FF", "#C2D1FF", "#A3BCFF", "#85A7FF"],
#         "Medium Warm": ["#FFE8D6", "#FFD1AD", "#FFBA85", "#FFA35C"],
#         "Deep Cool":   ["#D4EDDA", "#A8D8B8", "#7BC396", "#4FAE74"],
#         "Deep Warm":   ["#F8D7DA", "#F1AFB5", "#EA8790", "#E35F6B"]
#     }

#     # Default palette if tone not found
#     return color_palettes.get(
#         skin_tone,
#         ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4"]
#     )




import cv2
import numpy as np
import colorsys
import os
import joblib

# Paths (model expected to be in same utils/ directory)
BASE_DIR = os.path.dirname(__file__)
CASCADE_PATH = os.path.join(BASE_DIR, "haarcascade_frontalface_default.xml")
MODEL_PATH = os.path.join(BASE_DIR, "skin_depth.pkl")

# Load Haar cascade once (module import)
_face_cascade = None
if os.path.exists(CASCADE_PATH):
    _face_cascade = cv2.CascadeClassifier(CASCADE_PATH)

# loader for ML depth model (called from app start)
def load_skin_model(path=MODEL_PATH):
    if os.path.exists(path):
        try:
            mdl = joblib.load(path)
            return mdl
        except Exception as e:
            print("Failed to load skin depth model:", e)
            return None
    else:
        print("Skin depth model not found at", path)
        return None

def _extract_face_roi(image):
    """Return the upper-face ROI (forehead + cheeks) or None."""
    if _face_cascade is None:
        return None
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = _face_cascade.detectMultiScale(gray, 1.1, 6)
    if len(faces) == 0:
        return None
    x, y, w, h = max(faces, key=lambda f: f[2] * f[3])
    # pad a bit and take upper 60% to include cheeks and forehead
    pad_w = int(w * 0.05)
    pad_h = int(h * 0.05)
    x0 = max(0, x - pad_w)
    y0 = max(0, y - pad_h)
    x1 = min(image.shape[1], x + w + pad_w)
    y1 = max(0, y + int(h * 0.6))  # upper 60%
    roi = image[y0:y1, x0:x1]
    return roi

def _skin_mask_from_roi(roi):
    """Return boolean mask of skin-like pixels inside ROI using HSV ranges and morphology."""
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    # Use multiple ranges to capture diverse skin tones while excluding white/blue/gray
    lower1 = np.array([0, 15, 40], dtype=np.uint8)
    upper1 = np.array([25, 255, 255], dtype=np.uint8)
    lower2 = np.array([160, 15, 40], dtype=np.uint8)  # capture some reds/pinks
    upper2 = np.array([179, 255, 255], dtype=np.uint8)
    mask1 = cv2.inRange(hsv, lower1, upper1)
    mask2 = cv2.inRange(hsv, lower2, upper2)
    mask = cv2.bitwise_or(mask1, mask2)
    # remove extremes: too bright (white) and too desaturated (gray/blue)
    # create brightness and saturation masks
    v = hsv[:, :, 2]
    s = hsv[:, :, 1]
    bright_mask = v < 250  # ignore pure white highlights
    sat_mask = s > 10      # require some saturation
    mask = cv2.bitwise_and(mask, mask, mask=bright_mask.astype(np.uint8))
    mask = cv2.bitwise_and(mask, mask, mask=sat_mask.astype(np.uint8))
    # morphological clean up
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=1)
    return mask

def _compute_color_features(skin_pixels):
    """
    Input skin_pixels: Nx3 BGR array
    Returns: brightness (0-1), warmth (r-b scaled), saturation (0-1), avg_rgb tuple
    """
    if len(skin_pixels) == 0:
        return None
    avg_bgr = np.mean(skin_pixels, axis=0)
    b, g, r = avg_bgr
    # convert to 0-1
    r_f, g_f, b_f = r/255.0, g/255.0, b/255.0
    h, s, v = colorsys.rgb_to_hsv(r_f, g_f, b_f)
    brightness = v
    saturation = s
    warmth = (r - b) / 255.0
    return brightness, warmth, saturation, (int(r), int(g), int(b))

def _map_depth_label(depth_label):
    """
    Map ML numeric label to text depth.
    We assume: 0 -> Light, 1 -> Medium, 2 -> Deep (consistent with provided model)
    """
    if depth_label is None:
        return None
    if isinstance(depth_label, (list, np.ndarray)):
        dl = int(depth_label[0])
    else:
        dl = int(depth_label)
    return {0: "Light", 1: "Medium", 2: "Deep"}.get(dl, "Medium")

def _map_undertone(brightness, warmth, saturation, avg_rgb):
    """
    Improved undertone decision:
    - Use hue direction, but exclude white/gray or strongly non-skin tones.
    - Return 'Warm' or 'Cool'. For borderline cases use neutral -> choose closest.
    """
    r, g, b = avg_rgb
    # If saturation very low (grayish), treat as Neutral; map to nearest (use warmth threshold)
    if saturation < 0.12:
        # use warmth sign but with higher threshold
        if warmth > 0.07:
            return "Warm"
        elif warmth < -0.07:
            return "Cool"
        else:
            # neutral -> choose based on (r - g) slightly
            return "Warm" if (r - b) > 0 else "Cool"

    # For colored pixels use hue direction more robustly
    # Convert RGB to hue (0-360)
    rf, gf, bf = r/255.0, g/255.0, b/255.0
    h, s, v = colorsys.rgb_to_hsv(rf, gf, bf)
    hue_deg = h * 360.0
    # Typical warm hue range roughly 0-80 and 320-360 (reds -> yellows)
    # Cool hues roughly 160-300 (greens->blues), mid region ~80-160 is ambiguous
    if (hue_deg <= 80) or (hue_deg >= 320):
        return "Warm"
    elif 160 <= hue_deg <= 300:
        return "Cool"
    else:
        # ambiguous hue: use warmth metric and yellowish indicator
        yellowish = min(r, g) / 255.0
        if warmth > 0.06 or yellowish > 0.18:
            return "Warm"
        else:
            return "Cool"

def get_complementary_colors(skin_tone):
    """
    Provide palette mapping for the six-tone scheme.
    """
    color_palettes = {
        "Light Warm":  ["#FFF2E6", "#FFE0B3", "#FFCC80", "#FFB84D"],
        "Light Cool":  ["#E6F3FF", "#B3D9FF", "#80BFFF", "#4D9FFF"],
        "Medium Warm": ["#FFE8D6", "#FFD1AD", "#FFBA85", "#FFA35C"],
        "Medium Cool": ["#E0E6FF", "#C2D1FF", "#A3BCFF", "#85A7FF"],
        "Deep Warm":   ["#F8D7DA", "#F1AFB5", "#EA8790", "#E35F6B"],
        "Deep Cool":   ["#D4EDDA", "#A8D8B8", "#7BC396", "#4FAE74"]
    }
    return color_palettes.get(skin_tone, ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4"])

def detect_skin_tone(image_path, depth_model=None):
    """
    Hybrid skin tone detector:
    - Loads face ROI (Haar)
    - Extracts skin pixels via HSV mask within face
    - Computes color features
    - Uses depth_model to predict Light/Medium/Deep (if provided)
    - Uses improved undertone rules to get Warm/Cool
    - Returns one of: Light/Medium/Deep + Warm/Cool -> e.g. "Medium Warm"
    """
    try:
        img = cv2.imread(image_path)
        if img is None:
            return "Medium Warm"

        roi = _extract_face_roi(img)
        if roi is None:
            # fallback: analyze central crop
            h, w = img.shape[:2]
            cy, cx = h//2, w//2
            r = min(h, w)//6
            roi = img[cy-r:cy+r, cx-r:cx+r].copy()
            if roi is None or roi.size == 0:
                return "Medium Warm"

        mask = _skin_mask_from_roi(roi)
        skin_pixels = roi[mask > 0]
        if len(skin_pixels) == 0:
            # fallback region inside roi
            ch, cw = roi.shape[:2]
            ccy, ccx = ch//2, cw//2
            region = roi[max(0, ccy-30):min(ch, ccy+30), max(0, ccx-30):min(cw, ccx+30)]
            if region.size == 0:
                return "Medium Warm"
            skin_pixels = region.reshape(-1, 3)

        features = _compute_color_features(skin_pixels)
        if features is None:
            return "Medium Warm"
        brightness, warmth, saturation, avg_rgb = features

        # Depth prediction via model if provided
        depth_text = None
        if depth_model is not None:
            # model expects feature vector [brightness, warmth, saturation]
            try:
                X = np.array([[brightness, warmth, saturation]])
                pred = depth_model.predict(X)
                depth_text = _map_depth_label(pred)
            except Exception as e:
                depth_text = None

        # fallback depth from brightness if no model
        if depth_text is None:
            if brightness < 0.35:
                depth_text = "Deep"
            elif brightness < 0.65:
                depth_text = "Medium"
            else:
                depth_text = "Light"

        undertone = _map_undertone(brightness, warmth, saturation, avg_rgb)

        final = f"{depth_text} {undertone}"
        return final

    except Exception as e:
        print("skin_tone error:", e)
        return "Medium Warm"
