# 🏃‍♀️ Player Re-Identification – Single Feed (AI Internship Assignment)

## 👩‍💻 Developed by: Himali Paneru  
**Submission for:** AI Internship
**Task Chosen:** Option 2 – Re-Identification in a Single Feed

---

## 🎯 Objective

To track and re-identify players in a single 15-second sports video.  
The goal is to ensure that each player maintains a **consistent ID** throughout the video, even when they briefly move out of the frame and reappear.

---

## 🧠 Approach

- Used a pretrained **YOLOv11** model for player detection.
- Calculated **centroids** of bounding boxes for each detected player.
- Assigned and tracked IDs using **Euclidean distance-based matching**.
- Displayed bounding boxes and player IDs using **OpenCV**.

---

## 📁 Project Structure

```
📂 player-reid-himali
├── main.py                  # Main tracking code
├── 15sec_input_720p.mp4     # Input video
├── README.md                # Project documentation (this file)
├── report.md                # Report explaining methodology
```

> ❗ **Note:**  
> The YOLOv11 model file (`yolov11.pt`) is not included in this repository due to GitHub’s 100 MB file size limit.  
> 🔗 [Download yolov11.pt here](https://drive.google.com/file/d/1-5fOSHOSB9UXyP_enOoZNAMScrePVcMD/view) and place it in the project folder.

---

## 🛠️ Requirements

Install the required packages with:

```bash
pip install ultralytics opencv-python numpy
```

---

## 🚀 How to Run

1. Place `main.py`, `15sec_input_720p.mp4`, and `yolov11.pt` in the same folder.
2. Run the script:

```bash
python main.py
```

3. A video window will open showing player bounding boxes and consistent IDs.

> Press **Esc** to stop the video.

---

## ✅ Output Example

- Players are detected in each frame.
- Even when players move out of the frame and return, they retain the **same ID**.
- Output is displayed in real-time using OpenCV.

---

## 🔍 Limitations & Improvements

- **Current limitation:** Simple centroid-based tracking can fail in crowded or fast-moving scenes.
- **Future improvements:**
  - Use advanced tracking methods like **Deep SORT**.
  - Incorporate **appearance-based features** (like jersey color).
  - Add a smoother temporal consistency model using Kalman filters.

---

## 📄 Report

Please refer to the `report.md` file for a detailed explanation of:
- Approach and techniques used
- Challenges faced
- Future enhancement ideas

---

## 📬 Contact

If you have any questions, feel free to reach out via email or GitHub.

---
