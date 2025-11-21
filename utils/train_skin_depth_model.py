import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# =============================
# 1. Load your dataset
# =============================
data = pd.read_csv("skin_care_dataset.csv")

X = data.drop(columns=["label"])
y = data["label"]

# =============================
# 2. Preprocess
# =============================
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# =============================
# 3. Train the model
# =============================
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)
model.fit(X_scaled, y)

# =============================
# 4. Save model (NO OLD MODEL LOADING!)
# =============================
joblib.dump(model, "utils/skin_depth_model.pkl")
joblib.dump(scaler, "utils/skin_depth_scaler.pkl")

print("✔ Skin depth model trained successfully using sklearn 1.7.2")
