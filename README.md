# 🧠 Deepfake Video Detection

A web-based Deepfake Detection project with **Flask** and **Streamlit** implementations.
Detects fake videos/images using a CNN-based deep learning model and provides real-time analysis.

---

### 📌 Overview

* **Flask-Version**: Classic web app interface with HTML templates.
* **Streamlit-Version**: Lightweight, interactive web app using Streamlit.
* Users can upload videos/images, and the app predicts whether content is real or deepfake.

---

### 🎯 Objective

* Detect deepfake content in videos and images.
* Compare Flask and Streamlit deployment approaches.
* Demonstrate end-to-end ML workflow: input → model inference → output.

---

### 🗂️ Folder Structure

```
Deepfake_Video_Detection/
├─ Flask-Version/       # Flask app
│   ├─ app.py
│   ├─ templates/
│   ├─ static/
│   └─ requirements.txt
├─ Streamlit-Version/   # Streamlit app
│   ├─ app.py
│   ├─ data/
│   └─ requirements.txt
├─ deepfake_model.pkl   # Pre-trained model
├─ .gitignore
└─ autopush.bat
```

---

### ⚙️ Requirements

* Python 3.8+
* Install dependencies for each version:

**Flask-Version**

```bash
cd Flask-Version
pip install -r requirements.txt
python app.py
```

Open browser at: `http://127.0.0.1:5000`

**Streamlit-Version**

```bash
cd Streamlit-Version
pip install -r requirements.txt
streamlit run app.py
```

Browser opens automatically (usually `http://localhost:8501`)

---

### 🧪 How to Test

1. Run the desired app (Flask or Streamlit).
2. Upload a sample video or image using the interface.
3. The app analyzes the input and displays **Real / Deepfake** prediction with confidence score.

---

### 🧩 Model Details

* **Type**: Pre-trained CNN-based deepfake detector.
* **Input**: Video frames or images.
* **Output**: Probability/confidence of content being real or fake.
* **File**: `deepfake_model.pkl`
* **Notes**: For large models, consider downloading from release assets instead of storing in repo.

---

### 🔧 Auto Push Script

Use `autopush.bat` to commit and push changes automatically:

```bat
@echo off
SETLOCAL
for /f "tokens=1-5 delims=/:. " %%d in ("%date% %time%") do (
    set datetime=%%d-%%e-%%f_%%g-%%h
)
set commitMessage=Auto update on %datetime%
git rev-parse --is-inside-work-tree >nul 2>&1
IF ERRORLEVEL 1 (
    echo Current folder is not a Git repository!
    pause
    exit /b
)
git add .
git commit -m "%commitMessage%"
git push origin main
echo ----------------------------------------
echo ✅ Auto push complete!
echo ----------------------------------------
pause
```

---

### 📌 .gitignore

```
__pycache__/
*.py[cod]
*.pyo
*.pyd
*.env
env/
venv/
ENV/
env.bak/
venv.bak/
*.sqlite3
*.db
*.log
.DS_Store
.idea/
.vscode/
*.swp
*.swo
*.egg-info/
dist/
build/
```

---

### 📝 Notes

* Keep **Flask** and **Streamlit** versions in separate folders to avoid conflicts.
* Include **sample input videos/images** for testing.
* `.gitignore` prevents committing temporary or virtual environment files.
* README now shows **clear instructions to run and test**, making it recruiter/interviewer-friendly.

---

### 📸 Optional: Demo Screenshot

*(Add a screenshot or GIF of the running app here to impress recruiters)*

```
![Deepfake Detection Demo](demo_screenshot.png)
```

---

### 🔖 Badges (Optional)

* Python 3.8+
* Flask 2.x
* Streamlit 1.x

```
![Python](https://img.shields.io/badge/python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-orange)
```
