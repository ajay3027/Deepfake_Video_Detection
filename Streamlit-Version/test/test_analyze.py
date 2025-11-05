from src.analyze_video import analyze_video
import os

def test_analyze_on_sample():
    sample = "data/sample_real.mp4"
    assert os.path.exists(sample)
    res = analyze_video(sample, model_path="models/demo_model.h5", sample_frames=5)
    assert "verdict" in res
    assert isinstance(res["avg_confidence"], float)
    assert isinstance(res["frame_probs"], list)
