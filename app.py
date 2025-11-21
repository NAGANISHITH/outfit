from flask import Flask, render_template, request, jsonify, session, redirect
import pandas as pd
import numpy as np
import cv2
import joblib
import os
from datetime import datetime
import requests
from werkzeug.utils import secure_filename
# from utils.skin_tone import detect_skin_tone, get_complementary_colors
from utils.skin_tone import load_skin_model, detect_skin_tone, get_complementary_colors

from utils.skin_type import detect_skin_type
from utils.chatbot import ChatBot
from PIL import Image
import ast
import traceback

app = Flask(__name__)
app.secret_key = '56df9fe416e1503f53142d70c61e68b9'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def load_datasets():
    try:
        outfit_df = pd.read_csv('outfit_dataset.csv')
    except Exception as e:
        print(f"Error loading outfit dataset: {e}")
        outfit_df = pd.DataFrame()
    try:
        skincare_df = pd.read_csv('skin_care_dataset.csv')
    except Exception as e:
        print(f"Error loading skincare dataset: {e}")
        skincare_df = pd.DataFrame()
    return outfit_df, skincare_df

def load_model():
    try:
        model_data = joblib.load('model.pkl')
        outfit_model = model_data['model']
        print(f"Loaded model with accuracy: {model_data.get('accuracy', 'Unknown')}")
    except Exception as e:
        print(f"Error loading model: {e}")
        model_data = {}
        outfit_model = None
    return model_data, outfit_model

outfit_df, skincare_df = load_datasets()
model_data, outfit_model = load_model()



#added code-----------------------------------------------------------


# Load skin depth ML model only once at startup
from utils.skin_tone import load_skin_model
skin_depth_model = load_skin_model()

if skin_depth_model:
    print("Skin depth model loaded successfully!")
else:
    print("Skin depth model NOT loaded!")


#ended code-------------------------------------------------------------------------

chatbot = ChatBot()

WEATHER_API_KEY = "56df9fe416e1503f53142d70c61e68b9"

def get_current_season():
    month = datetime.now().month
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Autumn'

def get_weather_data(city="London"):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(url, timeout=5)
        if response.ok:
            data = response.json()
            return {
                'temperature': data['main']['temp'],
                'weather': data['weather'][0]['description'],
                'city': data['name']
            }
        else:
            print("Weather API non-200 response.")
    except Exception as e:
        print(f"Weather API error: {e}")
    return {'temperature': 20, 'weather': 'clear sky', 'city': city}

def predict_outfit(gender, occasion, skin_tone, season, temperature):
    try:
        if outfit_model and not outfit_df.empty:
            try:
                le_gender = model_data['le_gender']
                le_occasion = model_data['le_occasion']
                le_skin_tone = model_data['le_skin_tone']
                le_season = model_data['le_season']
                le_outfit = model_data['le_outfit']
                gender_encoded = le_gender.transform([gender])[0]
                occasion_encoded = le_occasion.transform([occasion])[0]
                skin_tone_encoded = le_skin_tone.transform([skin_tone])[0]
                season_encoded = le_season.transform([season])[0]
                features = [[gender_encoded, occasion_encoded, skin_tone_encoded, season_encoded, temperature]]
                prediction = outfit_model.predict(features)[0]
                outfit_name = le_outfit.inverse_transform([prediction])[0]
                matching_outfit = outfit_df[outfit_df['outfit_name'] == outfit_name].iloc[0]
                color_palette_str = matching_outfit['color_palette']
                try:
                    color_palette = ast.literal_eval(color_palette_str)
                except:
                    color_palette = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
                return {
                    'outfit_name': matching_outfit['outfit_name'],
                    'color_palette': color_palette,
                    'image_url': matching_outfit['image_url'],
                    'amazon_link': matching_outfit['amazon_link'],
                    'flipkart_link': matching_outfit['flipkart_link'],
                    'meesho_link': matching_outfit['meesho_link'],
                    'prediction_method': 'ML Model'
                }
            except Exception as e:
                print(f"Error in ML prediction: {e}")
        # Fallback: dataset search
        if not outfit_df.empty:
            filtered_df = outfit_df[
                (outfit_df['gender'].str.lower() == gender.lower()) &
                (outfit_df['occasion'].str.lower() == occasion.lower()) &
                (outfit_df['skin_tone'].str.lower() == skin_tone.lower()) &
                (outfit_df['season'].str.lower() == season.lower())
            ]
            if filtered_df.empty:
                filtered_df = outfit_df[
                    (outfit_df['gender'].str.lower() == gender.lower()) &
                    (outfit_df['occasion'].str.lower() == occasion.lower())
                ]
            if filtered_df.empty:
                filtered_df = outfit_df[outfit_df['gender'].str.lower() == gender.lower()]
            if not filtered_df.empty:
                best_match = filtered_df.iloc[0]
                color_palette_str = best_match['color_palette']
                try:
                    color_palette = ast.literal_eval(color_palette_str)
                except:
                    color_palette = get_complementary_colors(skin_tone)
                return {
                    'outfit_name': best_match['outfit_name'],
                    'color_palette': color_palette,
                    'image_url': best_match['image_url'],
                    'amazon_link': best_match['amazon_link'],
                    'flipkart_link': best_match['flipkart_link'],
                    'meesho_link': best_match['meesho_link'],
                    'prediction_method': 'Dataset Search'
                }
        # Fallback hardcoded
        return {
            'outfit_name': f'{occasion} Outfit for {skin_tone} Skin',
            'color_palette': get_complementary_colors(skin_tone),
            'image_url': '/static/images/default_outfit.jpg',
            'amazon_link': '#',
            'flipkart_link': '#',
            'meesho_link': '#',
            'prediction_method': 'Fallback'
        }
    except Exception as e:
        print(f"Prediction error: {e}")
        return {
            'outfit_name': 'Unknown',
            'color_palette': [],
            'image_url': '/static/images/default_outfit.jpg',
            'amazon_link': '#',
            'flipkart_link': '#',
            'meesho_link': '#',
            'prediction_method': 'Error'
        }

def get_skincare_recommendations(skin_type):
    try:
        if skincare_df.empty: return []
        recommendations = skincare_df[skincare_df['skin_type'].str.lower() == skin_type.lower()]
        return recommendations.head(3).to_dict('records')
    except Exception as e:
        print(f"Skincare rec error: {e}")
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        gender = request.form.get('gender')
        occasion = request.form.get('occasion')
        city = request.form.get('city', 'London')

        # Use uploaded image if given, otherwise use image from session
        file = request.files.get('image')
        if file and file.filename != '':
            filename = secure_filename(file.filename)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_')
            filename = timestamp + filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            session['uploaded_image'] = filepath
        elif session.get('uploaded_image'):
            filepath = session['uploaded_image']
        else:
            return jsonify({'error': 'No image selected'}), 400

        # Analyze skin tone and type
        #changed code-----------------------------------------------------------------
        #skin_tone = detect_skin_tone(filepath)


        skin_tone = detect_skin_tone(filepath, depth_model=skin_depth_model)

        
        #ended code----------------------------------------------------------------------------
        skin_type = detect_skin_type(filepath)

        # Weather, prediction, etc
        weather_data = get_weather_data(city)
        season = get_current_season()
        print(">>> Predict outfit inputs:", gender, occasion, skin_tone, season, weather_data['temperature'])
        outfit_prediction = predict_outfit(gender, occasion, skin_tone, season, weather_data['temperature'])
        skincare_recommendations = get_skincare_recommendations(skin_type)
        print(">>> Skincare recommendations:", outfit_prediction, skincare_recommendations)
        session['analysis_results'] = {
            'gender': gender,
            'occasion': occasion,
            'skin_tone': skin_tone,
            'skin_type': skin_type,
            'season': season,
            'weather': weather_data,
            'outfit': outfit_prediction,
            'skincare': skincare_recommendations,
            'uploaded_image': filepath.replace('\\', '/')
        }

        # Return for AJAX or redirect (depending on frontend)
        return jsonify({'success': True, 'redirect': '/results'})
    except Exception as e:
        print(f"Analysis error: {e}")
        traceback.print_exc()
        return jsonify({'error': f'Analysis failed: {str(e)}'}), 500

@app.route('/results')
def results():
    analysis_results = session.get('analysis_results')
    if not analysis_results:
        return redirect('/')
    return render_template('result.html', results=analysis_results)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        message = request.json.get('message', '')
        skin_type = session.get('analysis_results', {}).get('skin_type', 'normal')
        response = chatbot.get_response(message, skin_type)
        return jsonify({'response': response})
    except Exception as e:
        print(f"Chat error: {e}")
        return jsonify({'response': 'Sorry, I encountered an error. Please try again.'})

@app.route('/debug')
def debug():
    status = {
        'outfit_dataset_loaded': not outfit_df.empty,
        'outfit_dataset_size': len(outfit_df) if not outfit_df.empty else 0,
        'skincare_dataset_loaded': not skincare_df.empty,
        'skincare_dataset_size': len(skincare_df) if not skincare_df.empty else 0,
        'model_loaded': outfit_model is not None,
        'model_accuracy': model_data.get('accuracy', 'N/A'),
        'current_season': get_current_season(),
        'upload_folder_exists': os.path.exists(app.config['UPLOAD_FOLDER'])
    }
    return jsonify(status)



if __name__ == '__main__':
    print("Starting AI Outfit and Skin Advisor...")
    print(f"Outfit dataset: {len(outfit_df)} records")
    print(f"Skincare dataset: {len(skincare_df)} records")
    print(f"Model loaded: {outfit_model is not None}")
    app.run(debug=True, port=5000, host='0.0.0.0')
