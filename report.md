# Player Re-Identification in a Single Feed – Report

## 👤 Developer: Himali Paneru  
## 🔧 Role: ML Intern Applicant  
## 🎯 Task: Option 2 – Re-Identification in a Single Feed

---

## ✅ Objective
To identify and track players in a 15-second sports video (`15sec_input_720p.mp4`) such that players who temporarily leave the frame and reappear are assigned the **same identity** throughout the video.

---

## 🧠 Methodology

1. **Model Used**:  
   Utilized the provided fine-tuned YOLOv11 model to detect players frame-by-frame.

2. **Player ID Assignment**:  
   - Calculated the **centroid** of each bounding box.
   - Compared with previous frame centroids using **Euclidean distance**.
   - If distance < threshold → same ID; otherwise → assign new ID.

3. **Tracking**:  
   - Stored and updated a dictionary of current player positions and IDs.
   - Used OpenCV to draw bounding boxes and display IDs.

---

## 🧪 Techniques Used

- **Object Detection**: YOLOv11 (Ultralytics version)
- **Distance-Based Tracking**: Centroid-based method
- **Visualization**: OpenCV for drawing rectangles and labels

---

## 🧩 Challenges Faced

- Slight movement or overlap between players sometimes caused ID switches.
- YOLOv11 occasionally missed detections for partially visible players.
- Centroid tracking works best for small numbers of players — could get confused in dense frames.

---

## 🚀 Future Improvements

- Add a proper tracking algorithm like **SORT** or **Deep SORT**.
- Integrate **appearance-based matching** (like color histograms or embeddings).
- Implement better handling for occlusions and overlapping detections.
- Explore temporal smoothing or Kalman filtering for more stable ID tracking.

---

## ✅ Conclusion

The solution successfully demonstrates a simple method of re-identifying players in a single video stream using object detection and centroid-based tracking. While improvements can be made, this baseline approach meets the goal of maintaining consistent player identities in real-time.

---