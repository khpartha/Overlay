# AI Eye Overlay Project – Real-Time Face Feature Augmentation
This project demonstrates a lightweight real-time AI face augmentation system that uses a standard webcam to detect human facial landmarks and apply custom eye overlays dynamically.
The system is built using Python, leveraging MediaPipe for facial landmark detection and OpenCV for real-time image processing and blending.

# Project Goals 
  - Detect a user's face and track key facial features (specifically the eyes) in real-time.
  - Overlay a custom-designed eye image over both the left and right eyes, automatically resizing and aligning them based on face position and size.
  - Ensure smooth visual blending using alpha transparency for a natural and responsive effect.

# Technologies Used
  - Python 3.10
  - OpenCV – For webcam access, image resizing, and pixel-level processing
  - MediaPipe FaceMesh – For high-precision facial landmark detection (468 points)
  - PNG image input – Custom eye designs with optional transparency

# Installation requirements
  - Make sure you have the right Python version, then install dependencies:

   ```bash
  pip install opencv-python mediapipe
 
```
  - Script installation

    ```bash
python -m venv venv
venv\Scripts\activate

 
```



# How It Works
  - The webcam captures video frames in real-time.
  - MediaPipe detects a face and extracts the positions of key landmarks around the eyes.
  - The application identifies the bounding box of each eye based on those landmarks.
  - A static eye image (PNG format) is resized and blended onto each detected eye using pixel-level alpha blending.
  - The augmented frame is displayed live, creating an illusion of virtual eyes that move and scale naturally with your face.
  - <img width="259" alt="image" src="https://github.com/user-attachments/assets/6c1fdbea-c3ba-46fb-86fb-c29ef4ced75c" />
# IMPORTANT NOTE!
  Use python 3.10 or below as the program is built for that purpose.


  

  








