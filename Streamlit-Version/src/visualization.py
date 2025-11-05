import matplotlib.pyplot as plt
import io
import numpy as np
from PIL import Image

def plot_confidence_trend(frame_probs):
    plt.figure(figsize=(6,3))
    plt.plot(frame_probs, marker='o')
    plt.title("Frame-wise Fake Confidence")
    plt.xlabel("Frame Index")
    plt.ylabel("Fake Probability")
    plt.grid(True)
    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return buf  # return buffer so Streamlit can read

def frames_to_pil_list(frames, max_show=6):
    pil_list = []
    for f in frames[:max_show]:
        pil = Image.fromarray(np.uint8(f))
        pil_list.append(pil)
    return pil_list
