# 🚀 FastAPI Object Detection with **YOLOv11** 🐍

Welcome to the **FastAPI + YOLOv11 Object Detection** project! This application leverages **FastAPI** to serve an API for object detection in video files using the **YOLOv11** model. The backend accepts video files, processes them frame-by-frame, and performs object detection on selected frames using a pretrained **YOLOv11 model**. The results are returned in a structured format. 

This is a great project for developers interested in deploying deep learning models using **FastAPI** and **YOLOv11** for object detection tasks. 🚀

---

## 🛠️ Features

- **FastAPI**: A fast, modern web framework for Python designed for high-performance APIs.
- **YOLOv11 Object Detection**: Detect objects in videos using the **YOLOv11 model**.
- **Video Processing**: Processes frames of a video and performs detection on selected frames.
- **GPU Support**: Utilizes GPU if available, for faster inference.
- **Batch Inference**: Efficiently processes multiple video frames for detection.
- **File Upload**: Upload a video file to the API and get back detection results.

---

## 📦 Requirements

This project is built with **Python 3.10** and requires the following dependencies:

- **Python 3.10+**: Make sure you're using Python 3.10 or higher for compatibility.
- **FastAPI**: A modern Python web framework for building APIs.
- **Uvicorn**: ASGI server to run FastAPI.
- **YOLOv11**: The latest version of YOLO (v11) for object detection.
- **OpenCV**: For video processing.
- **Torch**: PyTorch library for running machine learning models.

### Install Dependencies:

Use the following command to install the required dependencies:

```bash
pip install fastapi uvicorn ultralytics torch opencv-python numpy
```

---

## ⚙️ How It Works

### YOLOv11 Object Detection

The **YOLOv11** model is loaded using the **Ultralytics YOLO** library. The model performs object detection on selected video frames. Here's how the system works:

1. **Model Initialization**:
   The YOLOv11 model is loaded from a `.pt` file. If a GPU is available, the model is moved to the GPU for faster inference.

   ```python
   self.model = YOLO("./models/yolo11n.pt")
   if torch.cuda.is_available():
       self.model.cuda()
   ```

2. **Video Frame Selection**:
   The video is processed frame-by-frame, but only **16 evenly spaced frames** are selected for object detection. This reduces computation time while still capturing the overall content of the video.

   ```python
   frame_indices = np.linspace(0, frame_count - 1, 16, dtype=int)
   ```

3. **Detection Process**:
   The selected frames are passed through the YOLOv11 model for object detection. The output includes bounding boxes, confidence scores, and object class IDs.

4. **Inference**:
   Each frame undergoes batch inference, which is optimized for speed. The results are returned in a structured format.

---

## 📝 API Endpoints

### `POST /detect`

This endpoint accepts a video file and performs object detection on selected frames.

#### Request

- **File (Multipart Form)**: Upload a video file in formats like `.mp4`, `.avi`, `.mov`, `.mkv`, or `.webm`.

#### Response

- **video_results**: A list of frames with object detection results. Each frame contains:
  - **frame**: The frame index.
  - **detections**: A list of detected objects in the frame, including:
    - **class**: The object class ID (integer).
    - **confidence**: The detection confidence score.
    - **bbox**: The bounding box coordinates `[x_min, y_min, x_max, y_max]`.

- **Error**: If no file is provided or if the file type is unsupported, the API will return an error message.

#### Example Response:

```json
{
  "video_results": [
    {
      "frame": 0,
      "detections": [
        {
          "class": 1,
          "confidence": 0.89,
          "bbox": [50.4, 100.2, 400.5, 300.7]
        },
        ...
      ]
    },
    ...
  ]
}
```

#### Example Request:

You can use **Postman** or **curl** to upload a video to the `/detect` endpoint:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/detect' \
  -F 'file=@your_video.mp4'
```

---

## 🏃‍♂️ Running the App

To run the FastAPI app locally:

1. **Start the app with Uvicorn**:

```bash
uvicorn main:app --reload
```

2. **Access the API**:
   - The app runs locally at `http://127.0.0.1:8000`.
   - The **Swagger UI** documentation is available at `http://127.0.0.1:8000/docs`.

---

## 🧑‍💻 How to Train the YOLOv11 Model

To train the **YOLOv11** model for your own object detection tasks, you need to follow these steps:

1. **Prepare Your Dataset**:  
   - Ensure your dataset is in **YOLO format**: Each image should have an accompanying text file with the format:
     ```
     class_id x_center y_center width height
     ```
   - The labels are normalized to the range `[0, 1]` based on the image dimensions.

2. **Install YOLOv11**:
   - You need to install the **YOLOv11** repository, which can be found at the official Ultralytics GitHub:
     [Ultralytics YOLOv11](https://github.com/ultralytics/yolov11)

3. **Train the Model**:
   - Once your data is ready, you can start the training by running:
     ```bash
     python train.py --data <data_config.yaml> --cfg <model_config.yaml> --weights yolov5s.pt --batch-size 16
     ```
   - Replace `<data_config.yaml>` and `<model_config.yaml>` with your respective config files.
   
4. **Monitor Training**:  
   The training process will generate logs, and you can monitor the progress via TensorBoard or the console output.

5. **Save the Model**:  
   Once the model is trained, you can save the weights (`yolo11n.pt`) and use them in this FastAPI app.

For a more detailed training guide, refer to the [YOLOv11 documentation](https://github.com/ultralytics/yolov11) on GitHub.

---

## 🔧 Why Use the Backend Structure from the Previous Template?

Using the backend structure from the previous template brings several advantages:

1. **Modular and Scalable**: The architecture is modular, with separate containers for MongoDB, MinIO, and ML services, ensuring the system is scalable and easy to extend.
2. **Docker Integration**: The previous template leverages **Docker Compose** to deploy the entire stack, including database and storage services, in isolated containers.
3. **CORS Middleware**: By using FastAPI's CORS middleware, the app is ready for integration with frontend applications, allowing cross-origin resource sharing.
4. **Database Integration**: By leveraging MongoDB for data storage, you can easily store and manage detection results, video metadata, or logs.
5. **GPU Optimization**: The ML service is configured to utilize NVIDIA GPUs, allowing faster model inference when processing video frames.

---

## 📂 Project Structure

```bash
fastapi_yolo/
├── main.py               # FastAPI app with detection logic
├── models/               # Directory to store YOLO model weights
│   └── yolo11n.pt        # Pretrained YOLOv11 model file
├── requirements.txt      # Python dependencies
├── Dockerfile            # Dockerfile for backend service
├── docker-compose.yml    # Docker Compose configuration
├── README.md             # Project documentation
```

---

## 🤝 Contributing

We welcome contributions! If you have ideas for improving the project or adding new features, feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is licensed under the **MIT License**.
