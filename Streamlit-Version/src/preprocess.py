import cv2
import numpy as np
from mtcnn import MTCNN

detector = MTCNN()

def extract_frames(video_path, max_frames=40, sample_rate=1):
    cap = cv2.VideoCapture(video_path)
    frames = []
    i = 0
    while True and len(frames) < max_frames:
        ret, frame = cap.read()
        if not ret:
            break
        if i % sample_rate == 0:
            frames.append(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        i += 1
    cap.release()
    return frames

def crop_face(frame_rgb):
    # returns cropped face or full frame if none found
    try:
        detections = detector.detect_faces(frame_rgb)
        if detections:
            x,y,w,h = detections[0]['box']
            x, y = max(0,x), max(0,y)
            return frame_rgb[y:y+h, x:x+w]
    except Exception:
        pass
    return frame_rgb
