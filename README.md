# 🧠 Deepfake Detection Projects

---

### 📌 Overview
This repository contains two implementations of **Deepfake Detection** using Python:

- **Flask-Version**: Web app built with Flask framework.  
- **Streamlit-Version**: Web app built with Streamlit framework.  

Both projects allow users to upload videos or images and detect deepfake content using pre-trained AI models.  

---

### 🎯 Objective
- Detect deepfake content in images and videos.  
- Compare two web frameworks (Flask vs Streamlit) for deployment.  
- Showcase end-to-end project: data input → model inference → results display.  

---

### 🗂️ Folder Structure
Deepfake-Detection/
├─ Flask-Version/ # Flask project
├─ Streamlit-Version/ # Streamlit project
└─.gitignore # Ignored files like venv, pycache


---

### 📊 Dataset / Input
- Users provide their **own videos/images** for testing.  
- Supported formats: `.mp4`, `.avi`, `.jpg`, `.png` (depending on app).  

---

### 🧩 Model Architecture
- Pre-trained deepfake detection model (CNN-based or similar).  
- Input: Image frame or video frame sequences.  
- Output: Prediction of **real** or **deepfake** content.  
- Deployed via web interface (Flask or Streamlit).  

---

### ⚙️ Requirements

- Python 3.8+  
- Install dependencies for each project:

**Flask-Version**
cd Flask-Version
pip install -r requirements.txt
python app.py
Open browser at: http://127.0.0.1:5000

**Streamlit-Version**
cd Streamlit-Version
pip install -r requirements.txt
streamlit run app.py
Browser opens automatically (usually http://localhost:8501)

🧪 How to Test

1.Run the app (Flask or Streamlit).

2.Upload a sample video/image in the interface.

3.Check the detection results displayed in the web app.
