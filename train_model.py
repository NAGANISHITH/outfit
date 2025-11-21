# import pandas as pd
# import numpy as np
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import LabelEncoder
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score, classification_report
# import joblib

# def create_and_train_model():
#     """Create and train the outfit recommendation model"""
    
#     try:
#         # Load dataset
#         df = pd.read_csv('outfit_dataset.csv')
#         print(f"Dataset loaded with {len(df)} records")
#         print("Columns:", df.columns.tolist())
        
#         # Check for missing values
#         print("\nMissing values:")
#         print(df.isnull().sum())
        
#         # Prepare features
#         le_gender = LabelEncoder()
#         le_occasion = LabelEncoder()
#         le_skin_tone = LabelEncoder()
#         le_season = LabelEncoder()
#         le_outfit = LabelEncoder()
        
#         # Encode categorical variables
#         df['gender_encoded'] = le_gender.fit_transform(df['gender'])
#         df['occasion_encoded'] = le_occasion.fit_transform(df['occasion'])
#         df['skin_tone_encoded'] = le_skin_tone.fit_transform(df['skin_tone'])
#         df['season_encoded'] = le_season.fit_transform(df['season'])
#         df['outfit_encoded'] = le_outfit.fit_transform(df['outfit_name'])
        
#         print(f"\nUnique values:")
#         print(f"Genders: {le_gender.classes_}")
#         print(f"Occasions: {le_occasion.classes_}")
#         print(f"Skin tones: {le_skin_tone.classes_}")
#         print(f"Seasons: {le_season.classes_}")
#         print(f"Outfits: {len(le_outfit.classes_)} different outfits")
        
#         # Features and target
#         X = df[['gender_encoded', 'occasion_encoded', 'skin_tone_encoded', 'season_encoded', 'temperature']]
#         y = df['outfit_encoded']
        
#         print(f"\nFeature matrix shape: {X.shape}")
#         print(f"Target vector shape: {y.shape}")
        
#         # Split data with stratification to ensure balanced classes
#         X_train, X_test, y_train, y_test = train_test_split(
#             X, y, test_size=0.3, random_state=42, stratify=y
#         )
        
#         print(f"Training set size: {len(X_train)}")
#         print(f"Test set size: {len(X_test)}")
        
#         # Train model with better parameters
#         model = RandomForestClassifier(
#             n_estimators=200,
#             max_depth=10,
#             min_samples_split=2,
#             min_samples_leaf=1,
#             random_state=42,
#             class_weight='balanced'
#         )
        
#         model.fit(X_train, y_train)
        
#         # Evaluate
#         y_pred = model.predict(X_test)
#         accuracy = accuracy_score(y_test, y_pred)
        
#         print(f"\nModel accuracy: {accuracy:.3f}")
#         print(f"Feature importance:")
#         feature_names = ['gender', 'occasion', 'skin_tone', 'season', 'temperature']
#         for name, importance in zip(feature_names, model.feature_importances_):
#             print(f"  {name}: {importance:.3f}")
        
#         # Save model and encoders
#         model_data = {
#             'model': model,
#             'le_gender': le_gender,
#             'le_occasion': le_occasion,
#             'le_skin_tone': le_skin_tone,
#             'le_season': le_season,
#             'le_outfit': le_outfit,
#             'accuracy': accuracy,
#             'feature_names': feature_names
#         }
        
#         joblib.dump(model_data, 'model.pkl')
#         print(f"\nModel saved successfully with {accuracy:.1%} accuracy!")
        
#         return model_data
        
#     except Exception as e:
#         print(f"Error in model training: {e}")
#         import traceback
#         traceback.print_exc()
#         return None

# def test_prediction():
#     """Test the trained model with sample data"""
#     try:
#         model_data = joblib.load('model.pkl')
#         model = model_data['model']
        
#         # Test prediction
#         test_input = [[0, 0, 0, 0, 20]]  # Female, Party, Light Cool, Winter, 20°C
#         prediction = model.predict(test_input)
#         print(f"Test prediction: {prediction}")
        
#     except Exception as e:
#         print(f"Error in test prediction: {e}")

# if __name__ == "__main__":
#     model_data = create_and_train_model()
#     if model_data:
#         test_prediction()





import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

def create_and_train_model():
    try:
        df = pd.read_csv("outfit_dataset.csv")
        print(f"Dataset loaded with {len(df)} records")

        # Encoders
        le_gender = LabelEncoder()
        le_occasion = LabelEncoder()
        le_skin_tone = LabelEncoder()
        le_season = LabelEncoder()
        le_outfit = LabelEncoder()

        # Encode columns
        df["gender_encoded"] = le_gender.fit_transform(df["gender"])
        df["occasion_encoded"] = le_occasion.fit_transform(df["occasion"])
        df["skin_tone_encoded"] = le_skin_tone.fit_transform(df["skin_tone"])
        df["season_encoded"] = le_season.fit_transform(df["season"])
        df["outfit_encoded"] = le_outfit.fit_transform(df["outfit_name"])

        # Remove rare classes (only 1 sample)
        counts = df["outfit_encoded"].value_counts()
        valid = counts[counts >= 2].index

        removed = len(df) - len(df[df["outfit_encoded"].isin(valid)])
        if removed > 0:
            print(f"\nRemoved {removed} rows that had only 1 sample each.")

        df = df[df["outfit_encoded"].isin(valid)]

        # Remaining dataset
        print(f"\nNew dataset size after cleaning: {len(df)} records")

        X = df[
            ["gender_encoded", "occasion_encoded", "skin_tone_encoded", "season_encoded", "temperature"]
        ]
        y = df["outfit_encoded"]

        num_classes = len(y.unique())
        num_samples = len(df)

        print(f"Classes: {num_classes}, Samples: {num_samples}")

        # -----------------------------------------
        # SMART SAFE SPLITTING LOGIC
        # -----------------------------------------

        # If dataset is too small, skip test split entirely
        if num_samples < 10 or num_classes < 3:
            print("\n⚠ Dataset too small for train/test split.")
            print("⚠ Training on the FULL dataset without splitting.")
            X_train, X_test, y_train, y_test = X, X, y, y
            stratify = None

        else:
            # If test_size < num_classes, disable stratify
            if int(num_samples * 0.3) < num_classes:
                print("\n⚠ Test set too small for stratification — disabling stratify.")
                stratify = None
            else:
                stratify = y

            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.3, random_state=42, stratify=stratify
            )

        # Train model
        model = RandomForestClassifier(
            n_estimators=200,
            max_depth=10,
            random_state=42,
            class_weight="balanced",
        )
        model.fit(X_train, y_train)

        # Evaluate
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)

        print(f"\nModel Accuracy: {acc:.3f}")

        # Save model
        model_data = {
            "model": model,
            "le_gender": le_gender,
            "le_occasion": le_occasion,
            "le_skin_tone": le_skin_tone,
            "le_season": le_season,
            "le_outfit": le_outfit,
            "accuracy": acc,
        }

        joblib.dump(model_data, "model.pkl")
        print("\nModel saved successfully!")

        return model_data

    except Exception as e:
        print("ERROR:", e)
        import traceback
        traceback.print_exc()
        return None


def test_prediction():
    try:
        data = joblib.load("model.pkl")
        model = data["model"]
        test_input = [[0, 0, 0, 0, 20]]
        print("Prediction:", model.predict(test_input))
    except Exception as e:
        print("Test error:", e)


if __name__ == "__main__":
    model_data = create_and_train_model()
    if model_data:
        test_prediction()
