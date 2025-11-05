import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.analyze_video import analyze_video
from src.visualization import plot_confidence_trend, frames_to_pil_list
import tempfile
from PIL import Image
import plotly.graph_objects as go
from fpdf import FPDF

st.set_page_config(
    page_title="Deepfake Video Detector",
    page_icon="🎭",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: #fafafa;
    font-family: 'Poppins', sans-serif;
}
h1, h2, h3 {
    color: #00f5d4;
    text-align: center;
    font-weight: 700;
    text-shadow: 0 0 15px #00f5d4;
}
.upload-box {
    border: 2px dashed #00f5d4;
    padding: 40px;
    border-radius: 20px;
    text-align: center;
    background: rgba(255, 255, 255, 0.05);
    box-shadow: 0 4px 30px rgba(0, 255, 255, 0.2);
    backdrop-filter: blur(6px);
}
.metric-box {
    background: rgba(255, 255, 255, 0.08);
    border-radius: 15px;
    padding: 15px;
    text-align: center;
}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🎭 Deepfake Detection Intelligence Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<h3>AI-powered system to detect manipulated or synthetic videos</h3>", unsafe_allow_html=True)
st.markdown("---")

st.sidebar.header("⚙️ Control Panel")
sample_opt = st.sidebar.radio(
    "Choose Mode:",
    ["Upload My Own Video", "Use Sample Real", "Use Sample Fake"]
)
st.sidebar.info("Upload or select a video for AI-based deepfake analysis")

if sample_opt == "Upload My Own Video":
    uploaded = st.file_uploader("📂 Upload your video (MP4 / AVI / MOV)", type=["mp4", "avi", "mov"])
elif sample_opt == "Use Sample Real":
    uploaded = open("data/sample_real.mp4", "rb")
elif sample_opt == "Use Sample Fake":
    uploaded = open("data/sample_fake.mp4", "rb")
else:
    uploaded = None

def generate_pdf(verdict, avg_conf, frame_probs):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 18)
    pdf.cell(0, 10, "Deepfake Detection Report", 0, 1, "C")
    pdf.set_font("Arial", "", 12)
    pdf.ln(10)
    pdf.cell(0, 10, f"Verdict: {verdict}", 0, 1)
    pdf.cell(0, 10, f"Average Fake Probability: {avg_conf:.2f}", 0, 1)
    pdf.ln(5)
    pdf.cell(0, 10, f"Frame Confidence Trend: {', '.join([f'{x:.2f}' for x in frame_probs[:10]])}...", 0, 1)
    tmp_path = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf").name
    pdf.output(tmp_path)
    return tmp_path

def plot_gauge(confidence):
    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=confidence * 100,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Fake Confidence (%)", 'font': {'size': 22, 'color': "#00f5d4"}},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#00f5d4"},
            'bar': {'color': "#00f5d4"},
            'bgcolor': "rgba(255,255,255,0.1)",
            'borderwidth': 2,
            'bordercolor': "#00f5d4",
            'steps': [
                {'range': [0, 50], 'color': "rgba(0,255,0,0.2)"},
                {'range': [50, 100], 'color': "rgba(255,0,0,0.2)"}
            ]
        }
    ))
    gauge.update_layout(paper_bgcolor="rgba(0,0,0,0)", font={'color': "#fafafa", 'family': "Poppins"})
    return gauge

if uploaded:
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    tmp.write(uploaded.read())
    st.video(tmp.name)

    with st.spinner("🔍 Analyzing video, please wait..."):
        res = analyze_video(tmp.name, model_path="models/deepfake_model.h5", sample_frames=25)

    st.markdown("---")
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(f"<h2>✅ Result: {res['verdict']}</h2>", unsafe_allow_html=True)
        st.metric("Average Fake Probability", f"{res['avg_confidence']:.2f}")
        buf = plot_confidence_trend(res['frame_probs'])
        st.image(buf, caption="Frame-wise Fake Confidence", use_column_width=True)

    with col2:
        gauge_fig = plot_gauge(res['avg_confidence'])
        st.plotly_chart(gauge_fig, use_container_width=True)

    st.subheader("🖼️ Key Frames")
    pil_list = frames_to_pil_list(res['sampled_frames'], max_show=6)
    cols = st.columns(len(pil_list))
    for i, p in enumerate(pil_list):
        cols[i].image(p, use_column_width=True)

    pdf_path = generate_pdf(res['verdict'], res['avg_confidence'], res['frame_probs'])
    with open(pdf_path, "rb") as f:
        st.download_button("📄 Download Analysis Report (PDF)", f, file_name="Deepfake_Report.pdf")

else:
    st.markdown('<div class="upload-box">⬆️ Upload or select a sample video from the sidebar to start analysis</div>', unsafe_allow_html=True)
