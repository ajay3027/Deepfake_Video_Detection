# features.py
import cv2
import mediapipe as mp
import numpy as np

mp_face = mp.solutions.face_mesh

def eye_aspect_ratio(eye):
    if len(eye) < 6:
        return 0.0
    A = np.linalg.norm(np.array(eye[1]) - np.array(eye[5]))
    B = np.linalg.norm(np.array(eye[2]) - np.array(eye[4]))
    C = np.linalg.norm(np.array(eye[0]) - np.array(eye[3]))
    return (A + B) / (2.0 * C)

def mouth_aspect_ratio(mouth):
    if len(mouth) < 2:
        return 0.0
    mouth = np.array(mouth)
    dists = [np.linalg.norm(mouth[i] - mouth[i+1]) for i in range(len(mouth)-1)]
    return float(np.mean(dists))

def extract_features(video_path):
    cap = cv2.VideoCapture(video_path)
    xs, ys, zs = [], [], []
    ears, mars = [], []
    frame_count = 0

    with mp_face.FaceMesh(static_image_mode=False, max_num_faces=1) as face_mesh:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame_count += 1
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = face_mesh.process(frame_rgb)

            if results.multi_face_landmarks:
                landmarks = results.multi_face_landmarks[0].landmark
                xs.extend([lm.x for lm in landmarks])
                ys.extend([lm.y for lm in landmarks])
                zs.extend([lm.z for lm in landmarks])

                # Eye landmarks
                left_eye = [(landmarks[i].x, landmarks[i].y) for i in [33, 160, 158, 133, 153, 144] if i < len(landmarks)]
                right_eye = [(landmarks[i].x, landmarks[i].y) for i in [362, 385, 387, 263, 373, 380] if i < len(landmarks)]
                mouth = [(landmarks[i].x, landmarks[i].y) for i in range(78, 88) if i < len(landmarks)]

                ears.append(eye_aspect_ratio(left_eye))
                ears.append(eye_aspect_ratio(right_eye))
                mars.append(mouth_aspect_ratio(mouth))

    cap.release()

    if len(xs) == 0:
        features = [0.0] * 11
    else:
        features = [
            float(np.mean(xs)), float(np.mean(ys)), float(np.mean(zs)),
            float(np.std(xs)), float(np.std(ys)), float(np.std(zs)),
            float(np.mean(ears)), float(np.std(ears)),
            float(np.mean(mars)), float(np.std(mars)),
            float(frame_count)
        ]

    print(f"[INFO] Extracted features length: {len(features)}")
    return features
