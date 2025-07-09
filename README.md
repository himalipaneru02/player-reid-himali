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

> **Note:** The YOLOv11 model file (`yolov11.pt`) is not included in this repository due to GitHub's 100MB file size limit.  
> You can download the model from the following link and place it in the same directory as `main.py`:

🔗 [Download yolov11.pt](https://drive.google.com/file/d/1-5fOSHOSB9UXyP_enOoZNAMScrePVcMD/view)
