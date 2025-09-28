# train.py
import os
from features import extract_features
from sklearn.ensemble import RandomForestClassifier
import joblib

REAL_PATH = "data/real"
FAKE_PATH = "data/fake"

X = []
y = []

print("[INFO] Extracting features from real videos...")
for filename in os.listdir(REAL_PATH):
    file_path = os.path.join(REAL_PATH, filename)
    features = extract_features(file_path)
    X.append(features)
    y.append(0)  # 0 = Real

print("[INFO] Extracting features from fake videos...")
for filename in os.listdir(FAKE_PATH):
    file_path = os.path.join(FAKE_PATH, filename)
    features = extract_features(file_path)
    X.append(features)
    y.append(1)  # 1 = Fake

print("[INFO] Training RandomForest model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

joblib.dump(model, "deepfake_model.pkl")
print("[INFO] Model saved as deepfake_model.pkl")
