# Player Re-Identification – Single Feed (AI Internship Assignment)

## 📌 Objective
To track and re-identify players in a single video feed (`15sec_input_720p.mp4`) such that players who leave the frame and return are assigned the same player ID throughout the clip.

## 🛠️ Tools & Libraries Used
- Python 3
- [Ultralytics YOLOv11](https://docs.ultralytics.com/)
- OpenCV
- NumPy

## 📁 Files
- `main.py`: Main script for player detection and ID tracking.
- `yolov11.pt`: Pretrained object detection model for detecting players (provided).
- `15sec_input_720p.mp4`: Input video (provided).
- `README.md`: This file.
- `report.md`: Project report (methodology, challenges, improvements).

## ⚙️ Setup Instructions

### 1. Install Dependencies
```bash
pip install ultralytics opencv-python numpy
