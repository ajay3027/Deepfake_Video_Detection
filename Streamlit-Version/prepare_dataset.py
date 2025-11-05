import cv2, os
from tqdm import tqdm

def extract_frames(video_path, output_dir, label, max_frames=5):
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    count = 0
    while count < max_frames:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, (640, 360))  # smaller frame = faster
        save_path = os.path.join(output_dir, f"{label}_{count}.jpg")
        cv2.imwrite(save_path, frame)
        count += 1
    cap.release()

def build_dataset(src_folder="data/train", dst_folder="data/frames_train"):
    for label in ["real", "fake"]:
        src_label = os.path.join(src_folder, label)
        dst_label = os.path.join(dst_folder, label)
        os.makedirs(dst_label, exist_ok=True)
        videos = [v for v in os.listdir(src_label) if v.endswith((".mp4", ".avi", ".mov"))]
        for vid in tqdm(videos, desc=f"Processing {label} videos"):
            extract_frames(os.path.join(src_label, vid), dst_label, label, max_frames=5)

if __name__ == "__main__":
    build_dataset()
