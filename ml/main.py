import cv2
from fastapi import FastAPI, UploadFile
from ultralytics import YOLO
import tempfile
import shutil
import torch
import numpy as np
import os

# Initialize FastAPI
app = FastAPI()

class Detection:
    def __init__(self):
        # Load the YOLO model and move to GPU
        self.model = YOLO("./models/yolo11n.pt")
        if torch.cuda.is_available():
            self.model.cuda()

    def detect(self, image):
        # Perform object detection on an image
        results = self.model(image)
        return results.pandas().xyxy[0].to_dict(orient="records")

    def process_video(self, video_path):
        # Open the video
        cap = cv2.VideoCapture(video_path)

        # Get total number of frames in the video
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        # Select 16 evenly spaced frames
        frame_indices = np.linspace(0, frame_count - 1, 16, dtype=int)

        # Prepare a list to store the results
        frame_results = []

        # Process the selected frames
        for idx in frame_indices:
            cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
            ret, frame = cap.read()
            if not ret:
                continue

            # Convert BGR to RGB for YOLO model compatibility
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Perform batch inference
            results = self.model.predict(frame_rgb)

            # Parse detections into a readable format
            detections = []
            for result in results:
                for box in result.boxes:
                    # Ensure bbox coordinates are flattened and converted to floats
                    bbox = box.xyxy[0].tolist() if isinstance(box.xyxy, torch.Tensor) else box.xyxy
                    detections.append({
                        "class": int(box.cls.item()),  # Convert to Python int
                        "confidence": float(box.conf.item()),  # Convert to Python float
                        "bbox": [float(coord) for coord in bbox]  # Flatten bbox coordinates
                    })

            frame_results.append({
                "frame": int(idx),  # Convert to Python int
                "detections": detections
            })

        # Release the video capture object
        cap.release()

        return frame_results


# Instantiate the detection class
detection_instance = Detection()

@app.post("/detect")
async def detect(file: UploadFile):
    """
    Endpoint to handle video file uploads and perform detection.
    """
    if not file:
        return {"error": "No file provided"}

    # Save the uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as tmp:
        shutil.copyfileobj(file.file, tmp)
        video_path = tmp.name

    # Check if the file is a video
    if video_path.endswith(('.mp4', '.avi', '.mov', '.mkv', '.webm')):
        results = detection_instance.process_video(video_path)
        # Cleanup temporary file
        os.remove(video_path)
        return {"video_results": results}
    else:
        # Cleanup temporary file
        os.remove(video_path)
        return {"error": "Unsupported file type"}