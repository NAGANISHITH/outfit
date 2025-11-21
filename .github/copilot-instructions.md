# AI Outfit & Skin Advisor - Agent Instructions

## Project Overview
This is a Flask-based web application that provides AI-powered outfit recommendations and skincare advice. The system integrates computer vision, machine learning, and external APIs to deliver personalized recommendations.

## Key Components & Architecture

### Core Services
- **Skin Analysis** (`utils/skin_tone.py`, `utils/skin_type.py`): 
  - Computer vision-based skin tone detection using HSV color space
  - Skin type classification (dry, oily, normal, combination)
  - Entry point through `/analyze` endpoint in `app.py`

- **Outfit Recommendation** (`app.py`, `outfit_dataset.csv`):
  - RandomForest model (`model.pkl`) for outfit matching
  - Considers skin tone, season, occasion, and weather
  - Weather data from OpenWeatherMap API integration

- **Chatbot System** (`utils/chatbot.py`):
  - Context-aware responses based on user's skin analysis
  - Accessed through `/chat` endpoint

### Data Flow
1. User uploads photo → Processed by skin analysis modules
2. Results stored in Flask session
3. Combined with weather API data and user preferences
4. Fed into ML model for recommendations
5. Results rendered through `templates/result.html`

## Development Workflow

### Environment Setup
```bash
pip install -r requirements.txt
python train_model.py  # Must be run before starting app
```

### Critical Configuration
- OpenWeatherMap API key required in `app.py`
- Max file upload size: 16MB (`app.py`)
- Session key for Flask app security

### Key Files for Common Tasks
- Adding new outfit recommendations: Update `outfit_dataset.csv`
- Modifying skin detection logic: `utils/skin_tone.py`
- UI customization: `static/css/style.css`, `templates/*.html`
- Chatbot responses: `utils/chatbot.py`

## Project Conventions
- Image processing uses OpenCV (BGR) → RGB conversion required
- Skin tone classifications: Light, Medium, Dark
- Temperature units: Celsius
- File uploads stored in `static/uploads/`

## Integration Points
- OpenWeatherMap API: Current weather conditions
- E-commerce links: Amazon, Flipkart, Meesho
- Image upload handling: Supports JPEG, PNG formats

For any changes to ML components, ensure `train_model.py` is re-run to update `model.pkl`.