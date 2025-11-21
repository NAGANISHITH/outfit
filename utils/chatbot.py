# import random
# import json

# class ChatBot:
#     def __init__(self):
#         self.responses = {
#             "greeting": [
#                 "Hello! I'm your AI beauty advisor. How can I help you today?",
#                 "Hi there! Ready to discover your perfect style?",
#                 "Welcome! I'm here to help with all your fashion and skincare needs!"
#             ],
#             "outfit": [
#                 "Based on your skin tone, I'd recommend colors that complement your natural beauty.",
#                 "Your outfit choice should consider both the occasion and your personal style.",
#                 "The right colors can really make your skin glow!"
#             ],
#             "skincare": {
#                 "dry": [
#                     "For dry skin, focus on hydration! Use gentle cleansers and rich moisturizers.",
#                     "Hyaluronic acid and ceramides are your best friends for dry skin.",
#                     "Don't forget to use a humidifier and drink plenty of water!"
#                 ],
#                 "oily": [
#                     "Oily skin needs balance. Use oil-free products and gentle exfoliation.",
#                     "Salicylic acid and niacinamide work wonders for oily skin.",
#                     "Don't skip moisturizer - even oily skin needs hydration!"
#                 ],
#                 "normal": [
#                     "Lucky you! Normal skin just needs a consistent, gentle routine.",
#                     "Focus on prevention with SPF and antioxidants.",
#                     "Maintain your skin's natural balance with gentle products."
#                 ],
#                 "combination": [
#                     "Combination skin requires a tailored approach for different areas.",
#                     "Use lighter products on your T-zone and richer ones on dry areas.",
#                     "Multi-masking can be great for combination skin!"
#                 ]
#             },
#             "glow_tips": [
#                 "Drink plenty of water and get enough sleep for natural glow!",
#                 "Regular exfoliation and moisturizing are key to glowing skin.",
#                 "Don't forget SPF - it's the best anti-aging product!",
#                 "A healthy diet rich in antioxidants shows on your skin.",
#                 "Face massage can improve circulation and give you that glow!"
#             ],
#             "color_advice": [
#                 "Warm undertones look great in gold, coral, and warm browns.",
#                 "Cool undertones shine in silver, blue, and cool pinks.",
#                 "Neutral undertones are lucky - most colors work for you!",
#                 "When in doubt, navy blue and white are universally flattering."
#             ]
#         }
    
#     def get_response(self, message, skin_type="normal"):
#         """
#         Generate chatbot response based on user message and skin type
#         """
#         message_lower = message.lower()
        
#         # Greeting responses
#         if any(word in message_lower for word in ["hello", "hi", "hey", "start"]):
#             return random.choice(self.responses["greeting"])
        
#         # Skincare advice
#         elif any(word in message_lower for word in ["skincare", "skin care", "routine", "products"]):
#             if skin_type in self.responses["skincare"]:
#                 return random.choice(self.responses["skincare"][skin_type])
#             return "I'd recommend consulting with a dermatologist for personalized skincare advice!"
        
#         # Glow tips
#         elif any(word in message_lower for word in ["glow", "glowing", "radiant", "bright"]):
#             return random.choice(self.responses["glow_tips"])
        
#         # Outfit advice
#         elif any(word in message_lower for word in ["outfit", "clothes", "fashion", "style", "wear"]):
#             return random.choice(self.responses["outfit"])
        
#         # Color advice
#         elif any(word in message_lower for word in ["color", "colours", "palette", "shade"]):
#             return random.choice(self.responses["color_advice"])
        
#         # Specific skin type questions
#         elif "dry skin" in message_lower:
#             return random.choice(self.responses["skincare"]["dry"])
#         elif "oily skin" in message_lower:
#             return random.choice(self.responses["skincare"]["oily"])
#         elif "combination skin" in message_lower:
#             return random.choice(self.responses["skincare"]["combination"])
        
#         # Default responses
#         else:
#             default_responses = [
#                 "That's an interesting question! Could you be more specific about what you'd like to know?",
#                 "I'm here to help with outfit suggestions and skincare advice. What would you like to know?",
#                 "Feel free to ask me about colors, outfits, skincare routines, or beauty tips!",
#                 f"Based on your {skin_type} skin type, I can give you personalized advice. What specifically interests you?"
#             ]
#             return random.choice(default_responses)
    
#     def get_product_recommendation(self, skin_type, concern="general"):
#         """
#         Get specific product recommendations
#         """
#         recommendations = {
#             "dry": {
#                 "cleanser": "Gentle cream cleanser with ceramides",
#                 "moisturizer": "Rich moisturizer with hyaluronic acid",
#                 "serum": "Hydrating serum with vitamin E"
#             },
#             "oily": {
#                 "cleanser": "Foaming cleanser with salicylic acid",
#                 "moisturizer": "Oil-free gel moisturizer",
#                 "serum": "Niacinamide serum for oil control"
#             },
#             "normal": {
#                 "cleanser": "Gentle daily cleanser",
#                 "moisturizer": "Balanced daily moisturizer",
#                 "serum": "Vitamin C serum for antioxidant protection"
#             },
#             "combination": {
#                 "cleanser": "Gentle foaming cleanser",
#                 "moisturizer": "Lightweight moisturizer",
#                 "serum": "Multi-targeted serum"
#             }
#         }
        
#         return recommendations.get(skin_type, recommendations["normal"])



# utils/chatbot.py
import random
import re
from typing import Optional

class ChatBot:
    """
    Expanded ChatBot for AI Outfit & Skin Advisor.

    - Rich multi-line response blocks (~10-15 lines each) for:
      * Outfit recommendations by undertone
      * Skincare routines per skin type
      * Medical skin issues (causes, signs, recovery)
      * Side-effect handling and recovery
      * General glow & safety tips

    Usage:
        bot = ChatBot()
        answer = bot.get_response("what colors suit warm undertone?", skin_type="normal")
    """

    def __init__(self):
        # Each value is a multi-line paragraph (string) or list of alternate multi-line paragraphs.
        self.responses = {
            # GREETINGS
            "greeting": [
                "Hello! I'm your AI beauty advisor. How can I help you today?\n"
                "I can help with outfit recommendations, color matching, skincare routines, and recovery from skincare side effects.\n"
                "Tell me your skin type or upload a photo for personalized advice.",

                "Hi there! Ready to discover your perfect style and skincare plan?\n"
                "Ask me about colors that suit your undertone, what to wear for an occasion, or how to treat common skin issues.\n"
                "I can provide step-by-step recovery tips if you've had an adverse reaction to a product."
            ],

            # OUTFIT recommendations keyed by undertone/skin color family
            "outfit_warm": [
                (
                    "Outfits for Warm Undertones — In-Depth Guide:\n"
                    "1) Color Palette: Favor golden, earthy tones: warm browns, terracotta, coral, mustard, olive, camel, warm reds, and gold accents.\n"
                    "2) Why: Warm undertones have yellow/golden base pigments; warm colors enhance the skin's natural glow and create harmony.\n"
                    "3) Fabric suggestions: Natural fibers with soft texture (linen, wool blends, silk-satin blends) reflect warm shades beautifully.\n"
                    "4) Patterns & contrasts: Try small to medium-scale prints with warm backgrounds; pair warm neutrals with a single vibrant accent (e.g., coral scarf).\n"
                    "5) Accessories: Gold jewelry, warm leather belts, and camel boots complement warm tones.\n"
                    "6) Seasonal adjustments: In summer, choose coral and warm white; in winter, deep rust and olive work well.\n"
                    "7) Makeup & coordination: Bronze eyeshadow and peachy blush harmonize with warm clothing choices.\n"
                    "8) Outfit ideas: Camel coat + olive sweater + warm-toned scarf; mustard dress with gold accessories for parties.\n"
                    "9) Balance tip: If wearing a very warm top, neutralize with cooler denim or off-white bottoms to avoid monochrome overload.\n"
                    "10) Confidence tip: test fabric and color in natural daylight; small changes (like a scarf) can reveal what truly flatters you."
                )
            ],

            "outfit_cool": [
                (
                    "Outfits for Cool Undertones — In-Depth Guide:\n"
                    "1) Color Palette: Prioritize cool blues, navy, icy pastels, lavender, cool pinks, true white, charcoal, and silver accents.\n"
                    "2) Why: Cool undertones have bluish or pinkish base pigments and look vibrant with colors that contain blue.\n"
                    "3) Fabric suggestions: Crisp cotton, silk, satin, and clean wool weaves keep cool palettes looking polished.\n"
                    "4) Patterns & contrasts: Use high-contrast combos like navy + white, or monochrome blue layers for sophistication.\n"
                    "5) Accessories: Silver or white gold jewelry, cool-toned gemstones, and sleek black or navy shoes.\n"
                    "6) Seasonal adjustments: In summer, choose icy blue and lavender; in winter, deep navy and plum are great.\n"
                    "7) Makeup & coordination: Cool-toned blush (soft pink) and cool highlighters pair well with these clothes.\n"
                    "8) Outfit ideas: Navy blazer + white shirt + charcoal trousers for office; lavender knit + jeans for casual.\n"
                    "9) Balance tip: If you want warmth, add a single neutral accessory like tan shoes but keep main palette cool.\n"
                    "10) Confidence tip: hold the garment near your face in natural light — cool undertones will make your skin appear fresher."
                )
            ],

            "outfit_neutral": [
                (
                    "Outfits for Neutral Undertones — In-Depth Guide:\n"
                    "1) Color Palette: Lucky you — neutral undertones can wear both warm and cool palettes: try olive, taupe, rose, navy, and muted jewel tones.\n"
                    "2) Why: Neutral undertones have balanced pigments; both warm and cool shades harmonize when chosen with depth in mind.\n"
                    "3) Fabric suggestions: Versatile fabrics like jersey, silk blends, and soft suiting fabrics work best across palettes.\n"
                    "4) Patterns & contrasts: Neutrals benefit from textured layers and tonal dressing (e.g., taupe + cream + cognac).\n"
                    "5) Accessories: Both gold and silver can work — choose based on the outfit's dominant palette.\n"
                    "6) Seasonal adjustments: Soft rose and cream for spring; olive and deep teal for fall.\n"
                    "7) Makeup & coordination: Neutral blush tones and balanced lip colors keep the look cohesive.\n"
                    "8) Outfit ideas: Tonal beige ensemble or mix of navy + blush for balanced contrast.\n"
                    "9) Balance tip: If a garment washes you out, add a bolder accessory (bright scarf, statement earring) to lift your complexion.\n"
                    "10) Confidence tip: experiment — neutrals often allow riskier pops of color with less chance of clashing."
                )
            ],

            # SKINCARE ROUTINES per skin type (multi-line)
            "skincare_dry": [
                (
                    "Skincare Routine for Dry Skin — Detailed Plan:\n"
                    "1) Cleanse gently with a cream or balm cleanser that preserves lipids; avoid harsh foaming agents.\n"
                    "2) Exfoliate sparingly (enzyme or very mild AHA once weekly) to remove flaky buildup without stripping oils.\n"
                    "3) Hydration layering: hydrating serum (hyaluronic acid) followed by a richer moisturizer with ceramides and fatty acids.\n"
                    "4) Use facial oils (rosehip, squalane) at night to strengthen barrier and lock moisture.\n"
                    "5) Humectants + occlusives: combine humectants (HA) with occlusives (petrolatum, dimethicone) when needed.\n"
                    "6) Sunscreen: broad-spectrum SPF 30+ daily; use moisturizing chemical or mineral sunscreens to avoid chalkiness.\n"
                    "7) Lifestyle: increase water intake, use humidifier in dry climates, avoid long hot showers.\n"
                    "8) Troubleshooting irritation: temporarily stop active ingredients (retinoids, strong acids) and use barrier-repair products.\n"
                    "9) Night care: sleep mask or overnight moisturizer 1–2x weekly for deep repair.\n"
                    "10) When to see a dermatologist: persistent redness, cracking, bleeding, or suspected eczema needs medical evaluation."
                )
            ],

            "skincare_oily": [
                (
                    "Skincare Routine for Oily / Acne-Prone Skin — Detailed Plan:\n"
                    "1) Use a gentle foaming cleanser twice daily to remove excess sebum without over-stripping.\n"
                    "2) Incorporate BHA (salicylic acid) 1–2% to penetrate pores and reduce comedones — start slowly.\n"
                    "3) Lightweight, non-comedogenic moisturizers (gel or lotion) to maintain barrier function.\n"
                    "4) Use niacinamide serums to reduce sebum production, inflammation, and strengthen barrier.\n"
                    "5) Retinoids at night (start low frequency) to normalize cell turnover and reduce acne lesions.\n"
                    "6) Sunscreen: oil-free formulations and mineral/chemical blends designed for oily skin.\n"
                    "7) Clay masks or absorbent treatments weekly for shine control but avoid overuse.\n"
                    "8) Avoid harsh scrubs and over-cleansing — they increase sebum rebound and irritation.\n"
                    "9) Troubleshooting breakouts: spot treat with benzoyl peroxide, but patch test to prevent irritation.\n"
                    "10) When to see a dermatologist: cystic acne, scarring, or persistent nodules require medical therapy."
                )
            ],

            "skincare_combination": [
                (
                    "Skincare Routine for Combination Skin — Detailed Plan:\n"
                    "1) Use a balanced gentle cleanser that won't dry the cheek areas while controlling the T-zone.\n"
                    "2) Consider using different products for different zones (multi-masking): heavier moisturizer on cheeks, gel on T-zone.\n"
                    "3) Use a light chemical exfoliant (PHA or BHA) on the T-zone and gentler acids on drier areas.\n"
                    "4) Niacinamide is versatile for combination skin — helps regulate oil and soothe dry patches.\n"
                    "5) Layering: hydrating serum + lightweight moisturizer; add oil to dry areas at night.\n"
                    "6) Sunscreen: broad-spectrum, lightweight lotion works well for mixed needs.\n"
                    "7) Clarifying masks for oily patches, hydrating sheet masks for dry areas, used alternately.\n"
                    "8) Avoid one-size-fits-all aggressive routines; treat zones according to their needs.\n"
                    "9) Troubleshooting: if flakes persist, add a gentle occlusive to dry zones; if oily breakouts persist, strengthen T-zone regimen.\n"
                    "10) When to see a dermatologist: severe, persistent or inflamed lesions and dermatitis across zones."
                )
            ],

            "skincare_normal": [
                (
                    "Skincare Routine for Normal Skin — Detailed Plan:\n"
                    "1) Maintain a simple daily routine: gentle cleanser, antioxidant serum (vitamin C), moisturizer, and SPF every morning.\n"
                    "2) Night care: consider a retinoid 2–3 times weekly to support collagen and cell turnover when tolerated.\n"
                    "3) Weekly exfoliation (mild AHA or enzyme) to keep texture smooth, but avoid over-exfoliation.\n"
                    "4) Hydration: light serums (HA) and moisturizers maintain balance without heaviness.\n"
                    "5) Use targeted products as needed: brightening serums for spots, lighter hydration in summer, richer at night in winter.\n"
                    "6) Lifestyle: balanced diet, sleep, SPF and antioxidant protection maintain skin health.\n"
                    "7) Preventative care: consistent SPF & antioxidants prevent premature aging and hyperpigmentation.\n"
                    "8) Troubleshooting: if sensitivity arises, simplify routine to 2–3 core products until recovery.\n"
                    "9) When to see a dermatologist: sudden changes in texture, persistent redness, or unusual lesions."
                )
            ],

            # GLOW and GENERAL TIPS
            "glow": [
                (
                    "Glow & Long-Term Skin Health — Practical Guide:\n"
                    "1) Hydration (internal and external) is the base: drink water and use humectants like hyaluronic acid.\n"
                    "2) Use sunscreen daily. Photodamage is the primary cause of dullness and uneven tone.\n"
                    "3) Antioxidants (vitamin C, E) protect from free radical damage and brighten over time.\n"
                    "4) Balanced exfoliation improves texture but avoid overuse — aim for gentle consistent use.\n"
                    "5) Diet & sleep: omega-3s, antioxidants, and restorative sleep support cellular recovery.\n"
                    "6) Regular gentle facial massage stimulates circulation for temporary glow.\n"
                    "7) Consistency over complexity: a few well-chosen products used regularly beat a regimen of random strong actives."
                )
            ],

            # COLOR ADVICE
            "color_advice": [
                (
                    "Color Advice — How to Use Color to Enhance Skin Tone:\n"
                    "1) Warm undertone: golds, corals, warm browns to create harmony and bounce warm light onto your face.\n"
                    "2) Cool undertone: blues, purples, cool pinks and gray-based neutrals to bring out clarity in your complexion.\n"
                    "3) Neutral undertone: experiment broadly — lean into muted jewel tones or rich neutrals.\n"
                    "4) Contrast: light-on-dark framing (e.g., white shirt under a dark jacket) brightens the face.\n"
                    "5) Balance: if wearing a bold color near the face, choose muted makeup to avoid color clash."
                )
            ],

            # MEDICAL SKIN ISSUES (each is long and includes causes, symptoms and recovery/when to see doc)
            "issue_acne": [
                (
                    "Acne — Causes, Signs, Immediate Care & Recovery Steps:\n"
                    "1) Causes: hormonal fluctuations, excess sebum, follicular hyperkeratinization, and bacteria (Cutibacterium acnes).\n"
                    "2) Symptoms: comedones, pustules, papules, nodules, inflammation and potential scarring in severe cases.\n"
                    "3) Immediate care: gentle cleansing, avoid aggressive picking, apply spot benzoyl peroxide or salicylic acid cautiously.\n"
                    "4) Avoid layering many active spot treatments at once; irritation leads to post-inflammatory hyperpigmentation.\n"
                    "5) Recovery plan: introduce evidence-based actives—topical retinoids (for comedonal acne), BPO for inflammatory lesions, topical antibiotics only as prescribed.\n"
                    "6) Scarring prevention: early control of inflammation, professional extraction by trained clinicians when needed.\n"
                    "7) Lifestyle: nutrition, sleep, and stress management can help; avoid occlusive cosmetics when prone to acne.\n"
                    "8) When to see a doctor: cysts, nodules, rapid spread, scarring or minimal response to OTC regimens — seek dermatology.\n"
                    "9) Prescription options: oral antibiotics, combined oral contraceptives (for hormonal acne), isotretinoin for severe recalcitrant cases.\n"
                    "10) Long-term: sustain maintenance therapy after clearing to prevent relapse (low-dose retinoid or topical therapy)."
                )
            ],

            "issue_eczema": [
                (
                    "Eczema (Atopic Dermatitis) — Causes, Immediate Care & Recovery:\n"
                    "1) Causes: genetic barrier dysfunction, immune dysregulation, environmental triggers, and allergens.\n"
                    "2) Symptoms: itchy, red, scaly patches, often in flexural areas; chronic scratching can cause lichenification.\n"
                    "3) Immediate care: stop suspected irritants, apply emollients liberally, and use cool compresses for itch.\n"
                    "4) Anti-inflammatory therapy: topical corticosteroids or non-steroidal alternatives (calcineurin inhibitors) as directed by a clinician.\n"
                    "5) Recovery steps: restore the skin barrier with frequent moisturization, gentle cleansers, and avoiding triggers (fragrances, harsh detergents).\n"
                    "6) Secondary infection: if pustules, crusting or fever occur, seek medical attention — antibiotics or antivirals may be required.\n"
                    "7) Phototherapy and systemic immunomodulators are options for severe or refractory disease under supervision.\n"
                    "8) Lifestyle: humidifiers, soft fabrics, and short lukewarm baths with emollient oils can help.\n"
                    "9) When to see a doctor: severe itching disrupting sleep, extensive involvement, or signs of infection.\n"
                    "10) Long-term: maintenance emollient therapy and trigger management reduce flares and improve quality of life."
                )
            ],

            "issue_rosacea": [
                (
                    "Rosacea — Causes, Signs & Management:\n"
                    "1) Causes: complex; vasculature, immune response, microbes and environmental triggers (heat, alcohol, spicy food).\n"
                    "2) Symptoms: central facial redness, flushing, visible blood vessels and sometimes acne-like bumps.\n"
                    "3) Immediate care: avoid known triggers, gentle skin care, and use soothing non-irritating products.\n"
                    "4) Medical therapy: topical metronidazole, azelaic acid, ivermectin or oral doxycycline for inflammatory rosacea.\n"
                    "5) Recovery steps: consistent prescribed therapy, sun protection and avoidance of vasodilating triggers.\n"
                    "6) Vascular treatments: pulsed-dye laser or IPL can reduce visible blood vessels in persistent cases.\n"
                    "7) Cosmetics: green-tinted primers and camouflage products help neutralize redness temporarily.\n"
                    "8) When to see a doctor: persistent or worsening redness, ocular symptoms (dryness or irritation), or progression despite avoidance measures.\n"
                    "9) Lifestyle: cool environment, gentle cleansers, and alcohol-free toners can reduce flares.\n"
                    "10) Long-term management: treat flares early and maintain trigger avoidance with supportive medical therapy."
                )
            ],

            "issue_allergic_contact": [
                (
                    "Allergic Contact Dermatitis — Immediate Care & Recovery:\n"
                    "1) Causes: topical allergens (fragrances, preservatives, nickel, rubber accelerators) trigger T-cell mediated reactions.\n"
                    "2) Symptoms: itchy, red, sometimes blistering rash appearing hours to days after exposure.\n"
                    "3) Immediate care: remove contact source, wash area with gentle soap, and apply cool compresses.\n"
                    "4) Short-term therapy: topical corticosteroids reduce inflammation; oral antihistamines may help with itch.\n"
                    "5) Patch testing: identify the allergen with formal patch testing if recurrent or widespread.\n"
                    "6) Recovery steps: avoid allergen once identified, use barrier creams and emollients to re-establish skin integrity.\n"
                    "7) Secondary infection risk: if secondarily infected, medical treatment (antibiotics) may be required.\n"
                    "8) Prevention: read labels, choose hypoallergenic products, and minimize new product introductions.\n"
                    "9) When to see a doctor: rapid spread, systemic symptoms, or failure to improve with basic measures.\n"
                    "10) Long-term: once allergen is identified, permanent avoidance prevents recurrence."
                )
            ],

            "issue_hyperpigmentation": [
                (
                    "Hyperpigmentation — Causes, Care & Fading Strategies:\n"
                    "1) Causes: post-inflammatory hyperpigmentation (PIH), sun damage, hormonal melasma, or medication-induced changes.\n"
                    "2) Symptoms: darker patches or spots that may persist for months after inflammation or sun exposure.\n"
                    "3) Immediate care: strict photoprotection (broad-spectrum SPF + physical barriers) to prevent darkening.\n"
                    "4) Topical therapies: hydroquinone (prescription), azelaic acid, kojic acid, niacinamide and retinoids help accelerate fading.\n"
                    "5) Professional options: chemical peels, IPL, microneedling and targeted lasers under dermatologic supervision.\n"
                    "6) Recovery steps: combine sun avoidance, topical inhibitors, and gentle exfoliation as tolerated.\n"
                    "7) Avoid strong irritating treatments if active inflammation is present — irritation worsens PIH.\n"
                    "8) Timeframe: expect gradual improvement over months; persistence is common without ongoing maintenance.\n"
                    "9) When to see a doctor: melasma worsening, extensive PIH or cosmetic concern — specialist therapies available.\n"
                    "10) Prevention: avoid picking acne, treat inflammation promptly, and use daily SPF."
                )
            ],

            # SIDE EFFECTS / RECOVERY from actives
            "side_effects_recovery": [
                (
                    "Handling Skin Irritation & Active Side Effects — Practical Steps:\n"
                    "1) Stop the suspected product immediately to prevent further damage.\n"
                    "2) Simplify to a barrier repair routine: gentle cleanser, fragrance-free emollient and SPF during daytime.\n"
                    "3) Avoid mixing multiple strong actives (e.g., retinoid + AHA/BHA + vitamin C) until recovered.\n"
                    "4) Short-term anti-inflammatory options: topical 1% hydrocortisone for small localized irritation (use briefly).\n"
                    "5) Cool compresses and oral antihistamines can help with itch and swelling.\n"
                    "6) Patch-test new products on the inner forearm for 48–72 hours before facial use.\n"
                    "7) If severe blistering, oozing, systemic symptoms or extensive involvement occur — seek medical attention immediately.\n"
                    "8) Recovery timeframe: minor irritations often improve within days; deeper damage may take weeks and benefit from ceramide-rich creams.\n"
                    "9) Reintroduction plan: reintroduce one product at a time, using low frequency and increasing as tolerated.\n"
                    "10) Prevention: educate on actives’ strengths, start low-and-slow, and always pair with barrier support."
                )
            ],

            # PRODUCT / ROUTINE ADVICE
            "product_advice": [
                (
                    "Product & Routine Advice — Choose Wisely:\n "
                    "1) Patch-test new serums or actives for 48–72 hours on the inner forearm.\n"
                    "2) Introduce one active at a time (e.g., retinoid) and build tolerance gradually.\n"
                    "3) Keep an eye on pH-sensitive pairing: strong acids and vitamin C vary in pH — layering matters.\n"
                    "4) Use sunscreen daily; many active products sensitize skin to UV.\n"
                    "5) Avoid excessive exfoliation; combine chemical and physical exfoliants cautiously."
                )
            ]
        }

        # Convert lists to strings joined by blank lines for easier display
        for k, v in list(self.responses.items()):
            if isinstance(v, list):
                # join list possible alternatives into one long string per key for consistent output
                self.responses[k] = "\n\n".join(v)

    def get_response(self, message: str, skin_type: Optional[str] = "normal") -> str:
        """
        Return an appropriate multi-line response string based on message contents and optional skin_type.
        """

        if not message:
            return self.responses.get("greeting", "Hello! How can I help?")

        msg = message.lower().strip()

        # Greeting
        if re.search(r"\b(hi|hello|hey|start|welcome)\b", msg):
            return self.responses.get("greeting")

        # Ask about outfits/colors
        if re.search(r"\b(what.*color|which colors|colors suit|what colors|color advice|colour)\b", msg):
            # try to detect undertone keywords
            if re.search(r"\b(warm|golden|yellow undertone|warm undertone)\b", msg):
                return self.responses.get("outfit_warm")
            if re.search(r"\b(cool|blue|pink undertone|cool undertone)\b", msg):
                return self.responses.get("outfit_cool")
            if re.search(r"\b(neutral|balanced undertone|neutral undertone)\b", msg):
                return self.responses.get("outfit_neutral")
            # fallback - ask skin_type or offer general color_advice
            return self.responses.get("color_advice")

        # Ask for outfit suggestions (general)
        if re.search(r"\b(outfit|dress|clothes|what to wear|wearing)\b", msg):
            # if mentions warm/cool/neutral in message
            if re.search(r"\b(warm|cool|neutral)\b", msg):
                # delegate to color rules above
                return self.get_response(msg, skin_type)
            # otherwise use color_advice + general outfit tips
            return self.responses.get("outfit_warm") + "\n\n" + self.responses.get("outfit_cool")

        # Skin type routines
        if re.search(r"\b(dry skin|i have dry|my skin is dry)\b", msg) or (skin_type and skin_type.lower() == "dry" and "skin" in msg):
            return self.responses.get("skincare_dry")
        if re.search(r"\b(oily skin|i have oily|my skin is oily|acne)\b", msg) or (skin_type and skin_type.lower() == "oily"):
            return self.responses.get("skincare_oily")
        if re.search(r"\b(combination skin|i have combination|my skin is combination)\b", msg) or (skin_type and skin_type.lower() == "combination"):
            return self.responses.get("skincare_combination")
        if re.search(r"\b(normal skin|i have normal skin|my skin is normal)\b", msg) or (skin_type and skin_type.lower() == "normal"):
            return self.responses.get("skincare_normal")

        # Glow tips
        if re.search(r"\b(glow|glowing|radiant|bright)\b", msg):
            return self.responses.get("glow")

        # Color advice
        if re.search(r"\b(color advice|color palette|palette|colour)\b", msg):
            return self.responses.get("color_advice")

        # Medical issues
        if re.search(r"\b(acne|pimple|zits|cystic)\b", msg):
            return self.responses.get("issue_acne")
        if re.search(r"\b(eczema|atopic|dermatitis)\b", msg):
            return self.responses.get("issue_eczema")
        if re.search(r"\b(rosacea|flushing|red face)\b", msg):
            return self.responses.get("issue_rosacea")
        if re.search(r"\b(allerg|contact dermatitis|allergic)\b", msg):
            return self.responses.get("issue_allergic_contact")
        if re.search(r"\b(hyperpigment|dark spot|melasma|post-inflammatory)\b", msg):
            return self.responses.get("issue_hyperpigmentation")

        # Side effects and recovery
        if re.search(r"\b(irritat|burn|stinging|peel|side effect|reaction)\b", msg):
            return self.responses.get("side_effects_recovery")

        # Product & routine guidance
        if re.search(r"\b(product|routine|how to use|introduce|patch test)\b", msg):
            return self.responses.get("product_advice")

        # If message mentions 'outfit' + an undertone, provide combined outfit advice
        if re.search(r"\b(outfit).*(warm|cool|neutral)\b", msg):
            return self.get_response(msg, skin_type)

        # Fallback: generic helpful prompts
        fallback = (
            "I'm here to help with outfits, colors, and skincare!\n"
            "Try asking more specifically, for example:\n"
            "- 'Which colors suit warm undertone?'\n"
            "- 'Best routine for oily skin?'\n"
            "- 'How to treat an irritated face after using retinol?'\n"
            "- 'Suggest outfits for a wedding with warm undertone.'\n"
            "If you'd like, tell me your skin type (dry, oily, combination, normal) or upload a photo for more tailored advice."
        )
        return fallback

    def get_product_recommendation(self, skin_type: str, concern: str = "general"):
        """
        Return structured product recommendations (string) for a given skin_type and concern.
        This is a helper to return quick targeted suggestions.
        """
        st = (skin_type or "normal").lower()
        recs = {
            "dry": {
                "cleanser": "Cream or balm cleanser (non-foaming).",
                "moisturizer": "Ceramide-rich moisturizer with fatty acids.",
                "serum": "Hyaluronic acid (multi-weight) serum.",
                "spot": "Not usually necessary; avoid alcohol-based products."
            },
            "oily": {
                "cleanser": "Gentle foaming cleanser with salicylic acid (1–2%) for morning/evening use as tolerated.",
                "moisturizer": "Oil-free, non-comedogenic gel moisturizer.",
                "serum": "Niacinamide 4-10% to regulate sebum and reduce inflammation.",
                "spot": "Benzoyl peroxide 2.5–5% for localized inflammatory lesions."
            },
            "combination": {
                "cleanser": "Balanced gentle cleanser; consider spot BHA on T-zone.",
                "moisturizer": "Lightweight lotion overall; richer cream for cheeks if needed.",
                "serum": "Niacinamide or low-strength vitamin C for tone balance.",
                "spot": "Benzoyl peroxide or salicylic acid for occasional breakouts."
            },
            "normal": {
                "cleanser": "Gentle daily cleanser.",
                "moisturizer": "Light to medium moisturizer depending on climate.",
                "serum": "Vitamin C antioxidant serum for brightness.",
                "spot": "Use targeted actives only when needed."
            }
        }
        chosen = recs.get(st, recs["normal"])
        # Optionally tailor by concern
        if concern and concern.lower() in ["acne", "breakout", "pimple"]:
            chosen["special"] = "Consider topical benzoyl peroxide or retinoid therapy; consult dermatologist for persistent acne."
        if concern and concern.lower() in ["dryness", "eczema", "barrier"]:
            chosen["special"] = "Barrier repair: ceramides, glycerin, occlusives; short-term topical steroid under doctor if inflamed."
        # Build return string
        lines = [f"Product recommendations for {skin_type} skin (concern: {concern}):"]
        for k, v in chosen.items():
            lines.append(f"- {k.title()}: {v}")
        return "\n".join(lines)


if __name__ == "__main__":
    # Quick interactive demo for local testing
    bot = ChatBot()
    print("Demo ChatBot (type 'quit' to exit). Try: 'what colors for warm undertone', 'my skin is oily', 'acne', 'irritation from retinol'.")
    while True:
        try:
            q = input("\nYou: ").strip()
            if not q:
                continue
            if q.lower() in ["quit", "exit"]:
                print("Bye!")
                break
            # optional: detect skin_type from a simple prefix like "skin: oily; question..."
            match = re.match(r"skin:\s*(\w+)\s*;\s*(.*)", q, flags=re.I)
            if match:
                skin = match.group(1)
                message = match.group(2)
            else:
                skin = "normal"
                message = q
            resp = bot.get_response(message, skin_type=skin)
            print("\nBot:\n")
            print(resp)
        except KeyboardInterrupt:
            print("\nInterrupted. Bye!")
            break
