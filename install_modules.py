import os

modules = [
    "numpy==1.25.2",
    "opencv-python==4.7.0.72",
    "mediapipe==0.10.21",
    "scikit-learn",
    "scipy",
    "pandas",
    "joblib",
    "matplotlib",
    "flask"
]

for module in modules:
    print(f"[INFO] Installing {module}...")
    os.system(f"pip install {module}")

print("[INFO] All modules installed successfully.")
