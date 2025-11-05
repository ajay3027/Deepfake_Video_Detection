from .model_utils import load_model, predict_frame
from .preprocess import extract_frames, crop_face
import numpy as np

def analyze_video(video_path, model_path="models/demo_model.h5", sample_frames=20):
    model = load_model(model_path)
    frames = extract_frames(video_path, max_frames=sample_frames, sample_rate=1)
    results = []
    sampled = []
    for f in frames:
        face = crop_face(f)
        p = predict_frame(model, face)
        results.append(p)
        sampled.append(face)
    avg = float(np.mean(results)) if results else 0.0
    verdict = "FAKE" if avg >= 0.5 else "REAL"
    return {
        "verdict": verdict,
        "avg_confidence": avg,
        "frame_probs": results,
        "sampled_frames": sampled
    }
