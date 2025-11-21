# AI-Based Outfit and Skin Advisor

A complete AI-powered web application that provides personalized outfit recommendations and skincare advice based on skin tone analysis, weather conditions, and user preferences.

## Features

### 🎨 AI-Powered Analysis
- **Skin Tone Detection**: Advanced computer vision algorithms analyze uploaded photos to determine skin tone
- **Skin Type Classification**: Automatic detection of skin type (dry, oily, normal, combination)
- **ML-Based Outfit Prediction**: RandomForest model trained on 500+ outfit combinations
- **Weather Integration**: Real-time weather data from OpenWeatherMap API

### 👗 Personalized Recommendations
- **Outfit Matching**: Tailored outfit suggestions based on gender, occasion, season, and skin tone
- **Color Palette**: Complementary color recommendations for your skin tone
- **E-commerce Integration**: Direct links to Amazon, Flipkart, and Meesho for shopping
- **Skincare Products**: Curated product recommendations based on detected skin type

### 🤖 AI Chatbot
- **Interactive Assistant**: Floating chatbot for style and beauty advice
- **Personalized Responses**: Context-aware responses based on your skin analysis
- **Beauty Tips**: Expert advice on skincare routines and outfit coordination

### 🎯 Modern UI/UX
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Smooth Animations**: Engaging micro-interactions and hover effects
- **Professional Styling**: Modern gradient backgrounds and glassmorphism effects
- **Intuitive Navigation**: User-friendly interface with clear visual hierarchy

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- OpenWeatherMap API key (free registration at openweathermap.org)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-outfit-skin-advisor
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Key**
   - Sign up for a free OpenWeatherMap API key at https://openweathermap.org/api
   - Replace `your_openweather_api_key` in `app.py` with your actual API key

4. **Train the ML Model**
   ```bash
   python train_model.py
   ```

5. **Create required directories**
   ```bash
   mkdir -p static/uploads
   mkdir -p static/images
   ```

6. **Run the application**
   ```bash
   python app.py
   ```

7. **Access the application**
   - Open your browser and navigate to `http://localhost:5000`

## Project Structure

```
ai-outfit-skin-advisor/
├── app.py                      # Main Flask application
├── model.pkl                   # Trained ML model
├── train_model.py             # Model training script
├── outfit_dataset.csv         # Outfit recommendations dataset
├── skin_care_dataset.csv      # Skincare products dataset
├── new_skintone.ipynb         # Original skin tone analysis notebook
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── utils/                     # Utility modules
│   ├── __init__.py
│   ├── skin_tone.py          # Skin tone detection logic
│   ├── skin_type.py          # Skin type classification
│   └── chatbot.py            # AI chatbot implementation
├── templates/                 # HTML templates
│   ├── index.html            # Main landing page
│   └── result.html           # Results display page
└── static/                   # Static assets
    ├── css/
    │   └── style.css         # Main stylesheet
    ├── js/
    │   └── script.js         # JavaScript functionality
    ├── images/               # Image assets
    └── uploads/              # User uploaded images
```

## Usage Guide

### 1. Upload Your Photo
- Click the upload area on the main page
- Select a clear photo of your face
- Supported formats: JPG, PNG (max 16MB)

### 2. Fill in Details
- **Gender**: Select your gender identity
- **Occasion**: Choose the event type (Party, Office, College, etc.)
- **City**: Enter your city for weather data

### 3. Get AI Analysis
- Click "Analyze My Style" to start the process
- Wait for AI to analyze your skin tone and type
- View your personalized results

### 4. Explore Recommendations
- **Outfit Suggestions**: See AI-recommended outfits with color palettes
- **Shopping Links**: Direct access to purchase similar items
- **Skincare Products**: Curated products for your skin type
- **Beauty Tips**: Chat with the AI assistant for more advice

## Technical Details

### Machine Learning Model
- **Algorithm**: Random Forest Classifier
- **Features**: Gender, Occasion, Skin Tone, Season, Temperature
- **Dataset**: 500+ outfit combinations with color palettes
- **Accuracy**: ~85% on test data

### Skin Analysis
- **Tone Detection**: HSV color space analysis with morphological operations
- **Type Classification**: Texture analysis using Local Binary Patterns
- **Categories**: Light/Medium/Deep with Cool/Warm undertones

### API Integration
- **Weather Data**: OpenWeatherMap API for real-time conditions
- **Season Detection**: Automatic based on current date
- **E-commerce**: Direct product links to major platforms

## Customization

### Adding New Outfits
1. Edit `outfit_dataset.csv`
2. Add new rows with required columns
3. Retrain the model: `python train_model.py`

### Adding Skincare Products
1. Edit `skin_care_dataset.csv`
2. Include product details and links
3. Restart the application

### Modifying Skin Analysis
- Update algorithms in `utils/skin_tone.py` and `utils/skin_type.py`
- Adjust color ranges and classification thresholds

## Troubleshooting

### Common Issues

1. **Model not found error**
   - Run `python train_model.py` to create the model file

2. **Weather API not working**
   - Check your API key in `app.py`
   - Ensure internet connection for API calls

3. **Image upload fails**
   - Check file size (max 16MB)
   - Ensure `static/uploads` directory exists

4. **Skin analysis errors**
   - Verify OpenCV installation
   - Use clear, well-lit photos for better results

### Performance Optimization
- Use smaller image sizes for faster processing
- Consider caching weather data for frequent requests
- Implement image compression for uploads

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenCV for computer vision capabilities
- Scikit-learn for machine learning algorithms
- Flask for web framework
- OpenWeatherMap for weather data
- Font Awesome for icons
- Google Fonts for typography

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review the project documentation
3. Create an issue on the repository
4. Contact the development team

---

**Note**: This application is for educational and demonstration purposes. For production deployment, consider additional security measures, error handling, and scalability optimizations.