# 🤖 Deepfake Detector 🎭

**Project:** 🌐 *Deepfake Detector* — a modular AI web app for detecting manipulated videos & images.

**Author:** 👨‍💻 Ajay Sharma

**Last updated:** 🗓️ October 24, 2025

---

## 📚 Table of Contents

1. [🎯 Project Overview](#project-overview)
2. [✨ Features](#features)
3. [🧩 Architecture & Tech Stack](#architecture--tech-stack)
4. [⚙️ Installation](#installation)
5. [🚀 Quick Start — Run Locally](#quick-start--run-locally)
6. [💻 Web App Usage](#web-app-usage)
7. [🧠 Model / Training](#model--training)
8. [📂 Datasets](#datasets)
9. [📊 Evaluation & Results](#evaluation--results)
10. [📁 Project Structure](#project-structure)
11. [🤝 Contributing](#contributing)
12. [🩵 Troubleshooting & FAQ](#troubleshooting--faq)
13. [⚖️ License & Acknowledgements](#license--acknowledgements)

---

## 🎯 Project Overview

This repository contains a **🌈 modular Deepfake Detector** — a web app that lets users upload images or short videos and analyzes them with AI to detect manipulations. 🕵️‍♂️

🎓 **Built as a college project**, it focuses on *clarity*, *modularity*, and *educational value* so each team member can work independently on UI, ML model, and evaluation.

**Goals:**

* 🧑‍💻 Build a clean, modular deepfake detection pipeline.
* 🌐 Provide an intuitive, easy-to-use web demo.
* 📊 Support reproducible ML experiments.

---

## ✨ Features

✅ Upload 🖼️ images or 🎥 short videos.
✅ Automatic frame extraction & face detection.
✅ Real vs Fake classification using a CNN 🧠.
✅ Confidence score with color indicators 🔵🟡🔴.
✅ Visual reports with graphs & confusion matrix 📈.
✅ Exportable results in CSV/JSON 📄.

---

## 🧩 Architecture & Tech Stack

🖥️ **Frontend:** HTML, CSS, JavaScript (single-page modular UI)
🐍 **Backend:** Flask / FastAPI
⚙️ **Model:** PyTorch (baseline CNN or ResNet/EfficientNet)
🎬 **Libraries:** OpenCV, Mediapipe, Scikit-learn, Pillow
📦 **Containerization:** Docker (optional)

---

## ⚙️ Installation

> 🧰 Tested on Windows 10 / Ubuntu 20.04 — Python 3.9+

```bash
git clone https://github.com/yourusername/Deepfake-Detector.git
cd Deepfake-Detector
```

Create & activate a virtual environment 🧪:

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
```

Install dependencies 🧰:

```bash
pip install -r requirements.txt
```

**requirements.txt** includes:

```
flask
torch
torchvision
opencv-python
numpy
scikit-learn
mediapipe
pillow
tqdm
```

---

## 🚀 Quick Start — Run Locally

Run Flask server 🧠:

```bash
python app/server.py
```

Open in browser 🌐:
👉 [http://localhost:5000](http://localhost:5000)

CLI inference 🖥️:

```bash
python app/infer.py --input path/to/video.mp4 --output results.json
```

🎬 The system will:

* Extract frames
* Detect faces
* Run classification
* Generate result summary ✅

---

## 💻 Web App Usage

🪄 **Steps:**

1. 🖱️ Click *Upload* and select image/video.
2. ⏳ Wait while processing…
3. 🎯 See prediction: **Real** 🟢 or **Fake** 🔴
4. 📥 Download full report (CSV/JSON).

⚙️ Change sampling rate or resolution in `config.yaml`.

---

## 🧠 Model / Training

Train your model with this command:

```bash
python train/train.py --data-dir data/train --epochs 20 --batch-size 32 --lr 0.001
```

🧩 Handles:

* Dataset loading
* Data augmentation
* Model checkpointing
* Logging + validation 📊

Save model in `models/` folder and use in inference.

---

## 📂 Datasets

Datasets used for research only:
📸 FaceForensics++
🎭 Celeb-DF
📹 DFDC

⚠️ **Note:** Respect dataset licenses & privacy laws.

---

## 📊 Evaluation & Results

Evaluate test results:

```bash
python eval/evaluate.py --predictions results/ --labels data/test/labels.csv
```

📈 **Sample Results:**

* Accuracy: 85%
* F1 Score: 0.82
* Confusion Matrix 📊

---

## 📁 Project Structure

```
Deepfake-Detector/
├─ app/
│  ├─ server.py
│  ├─ infer.py
│  ├─ utils.py
│  └─ static/
├─ train/
│  ├─ train.py
│  └─ dataset.py
├─ eval/
│  └─ evaluate.py
├─ models/
├─ data/
├─ requirements.txt
├─ Dockerfile
├─ README.md
└─ config.yaml
```

---

## 🤝 Contributing

💡 Fork the repo → Create a branch → Commit → Push → PR 🚀

Please add small tests or examples with any new feature.

---

## 🩵 Troubleshooting & FAQ

🧍‍♂️ **Face not detected?** Try switching detector backend in `config.yaml`.
🐢 **Slow inference?** Reduce frame rate or resolution.
⚠️ **Model load error?** Check architecture compatibility.

---

## 🧘 Ethical Considerations

🚫 This tool is **for education & awareness**, not surveillance.
💬 Always credit datasets & sources.
🔒 Respect privacy and responsible AI ethics.

---

## ⚖️ License & Acknowledge
