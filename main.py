import cv2
from ultralytics import YOLO
import numpy as np

# Load the model
model = YOLO('yolov11.pt')

# Initialize video
cap = cv2.VideoCapture('15sec_input_720p.mp4')
player_id = 0
players = {}

# Define distance threshold
DIST_THRESHOLD = 50

def get_centroid(box):
    x1, y1, x2, y2 = box
    return int((x1 + x2) / 2), int((y1 + y2) / 2)

frame_num = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)[0]
    boxes = results.boxes.xyxy.cpu().numpy()

    curr_players = {}

    for box in boxes:
        x1, y1, x2, y2 = box[:4]
        centroid = get_centroid((x1, y1, x2, y2))

        matched = False
        for pid, prev_centroid in players.items():
            dist = np.linalg.norm(np.array(prev_centroid) - np.array(centroid))
            if dist < DIST_THRESHOLD:
                curr_players[pid] = centroid
                matched = True
                break

        if not matched:
            player_id += 1
            curr_players[player_id] = centroid

        for pid, centroid in curr_players.items():
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame, f"Player {pid}", (int(x1), int(y1) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    players = curr_players.copy()
    cv2.imshow('Tracking', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()