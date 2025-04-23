import cv2
import mediapipe as mp

# Initialize MediaPipe FaceMesh and drawing utils
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Load anime eye PNG (with alpha channel)
anime_eye = cv2.imread("e.png", cv2.IMREAD_UNCHANGED)  # shape: (H, W, 4)

# Open webcam
cap = cv2.VideoCapture(0)

# Eye landmark indices
LEFT_EYE = [33, 133, 160, 159, 158, 153, 144, 145]
RIGHT_EYE = [362, 263, 387, 386, 385, 384, 398, 466]

# Function to overlay anime eye on a given eye region
def overlay_eye(frame, face_landmarks, eye_indices, w, h):
    eye_points = []
    for idx in eye_indices:
        pt = face_landmarks.landmark[idx]
        x, y = int(pt.x * w), int(pt.y * h)
        eye_points.append((x, y))

    x_coords = [p[0] for p in eye_points]
    y_coords = [p[1] for p in eye_points]
    x_min, x_max = min(x_coords), max(x_coords)
    y_min, y_max = min(y_coords), max(y_coords)

    padding = 5
    x_min = max(x_min - padding, 0)
    x_max = min(x_max + padding, w)
    y_min = max(y_min - padding, 0)
    y_max = min(y_max + padding, h)

    eye_width = x_max - x_min
    eye_height = y_max - y_min

    if eye_width > 0 and eye_height > 0:
        anime_resized = cv2.resize(anime_eye, (eye_width, eye_height))

        if anime_resized.shape[2] == 4:
            eye_rgb = anime_resized[:, :, :3]
            eye_alpha = anime_resized[:, :, 3] / 255.0
        else:
            eye_rgb = anime_resized
            eye_alpha = 1.0

        roi = frame[y_min:y_max, x_min:x_max]

        for c in range(3):
            roi[:, :, c] = roi[:, :, c] * (1 - eye_alpha) + eye_rgb[:, :, c] * eye_alpha

        frame[y_min:y_max, x_min:x_max] = roi

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            overlay_eye(frame, face_landmarks, LEFT_EYE, w, h)
            overlay_eye(frame, face_landmarks, RIGHT_EYE, w, h)

    cv2.imshow("Anime Eye Overlay", frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
