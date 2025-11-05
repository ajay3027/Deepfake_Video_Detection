# app.py
from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
import joblib
from features import extract_features
import webbrowser
import threading

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load trained model
try:
    model = joblib.load("deepfake_model.pkl")
    print("[INFO] Model loaded successfully.")
except Exception as e:
    print(f"[ERROR] Could not load model: {e}")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        if "video" not in request.files:
            prediction = "No video uploaded"
            return render_template("index.html", prediction=prediction)

        file = request.files["video"]
        if file.filename == "":
            prediction = "No selected video"
            return render_template("index.html", prediction=prediction)

        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(file_path)
        print(f"[INFO] File saved: {file_path}")

        try:
            features = extract_features(file_path)
            features = [features]  # model expects 2D array
            pred = model.predict(features)[0]
            prediction = "FAKE" if pred == 1 else "REAL"
        except Exception as e:
            print(f"[ERROR] Prediction failed: {e}")
            prediction = "Error in prediction"

    return render_template("index.html", prediction=prediction)

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == "__main__":
    # Launch browser in a separate thread after server starts
    threading.Timer(1, open_browser).start()
    app.run(debug=True)
