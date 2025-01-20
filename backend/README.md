# 🚀 FastAPI + MongoDB + MinIO Template for Juniors 🎉

Welcome to the **FastAPI Template Project**! This template is designed to help junior developers understand how to set up a full-stack web application using **FastAPI**, **MongoDB**, and **MinIO** for file storage. Whether you're looking to create an API with FastAPI or integrate file storage with MinIO and MongoDB, this is a great starting point. 🌱

This project is built to be easy to follow and includes **Docker** support to help you deploy it effortlessly. Let’s dive in! 😎

## 🛠️ Features

- **FastAPI Backend**: Build modern APIs fast with this Python web framework.
- **MongoDB**: A NoSQL database to store data in a flexible, JSON-like format.
- **MinIO**: A high-performance object storage system compatible with Amazon S3.
- **Docker**: Easily deploy the app in containers for easy scalability and portability.
- **CORS Middleware**: Allows cross-origin requests, perfect for APIs consumed by frontend applications.
- **Swagger UI**: Automatically generated documentation for your API, available at `/docs`! 📑

## ⚙️ Project Setup

This FastAPI project is designed with **junior developers** in mind. Below is the detailed setup for the components used:

### 1. **FastAPI App**

The core of the application is built using **FastAPI**, which is a modern Python web framework. FastAPI helps you build APIs quickly while ensuring high performance.

```python
from fastapi import FastAPI, HTTPException
app = FastAPI(title="My app", root_path="/my_app")
```

This code initializes the FastAPI app with the title `My app`. We also specify the root path for the app as `/my_app`.

- **FastAPI** provides auto-generated API docs using Swagger UI. 🎨
- **Routes** like `/` are defined using decorators (e.g., `@app.get("/")`).
  
### 2. **MongoDB Setup**

This app uses **MongoDB** to store data. MongoDB is a flexible, schema-less database where you can store JSON-like documents.

```python
from pymongo import MongoClient
MONGO_URI = os.getenv('MONGODB', "mongodb://clevtech:clevtech@mongodb:27017/")
mongo_client = MongoClient(MONGO_URI)
db = mongo_client["my_db"]
collection = db["my_collection"]
```

- **MongoDB URI**: The URI connects to MongoDB, using the `clevtech` credentials (which are customizable through environment variables).
- **Database & Collection**: The app connects to a database called `my_db` and a collection called `my_collection`. You can replace these with your own settings!

### 3. **MinIO Setup**

**MinIO** is an object storage system, great for handling files such as images, videos, and other media. It's compatible with Amazon S3, so you can easily integrate it into projects.

```python
from minio import Minio
minio_client = Minio(
    "minio:9000",
    access_key="clevtech",
    secret_key="clevtech",
    secure=False
)
```

- **MinIO Configuration**: The app connects to the MinIO service running on `minio:9000`. You can configure the access key and secret key for secure access.
- **Bucket Creation**: If the `files` bucket doesn't exist, it gets created automatically. This bucket will be used to store your files.

### 4. **CORS Middleware**

To enable cross-origin requests from other domains (like frontend applications), we’ve added **CORS middleware**.

```python
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

This setup ensures that any origin can interact with the API, making it ideal for frontend-backend communication. 🌐

### 5. **Static Files**

If you want to serve static files, FastAPI also makes it easy. This project is set up to serve static files, if needed.

```python
from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="static"), name="static")
```

### 6. **Root Endpoint**

The root endpoint (`/`) simply returns a friendly greeting. It’s the first API route you’ll see when you access your app.

```python
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
```

### 7. **Environment Configuration**

- **MongoDB**: You can configure the MongoDB URI with the `MONGODB` environment variable.
- **MinIO**: MinIO’s access and secret keys can also be set in the environment.
- **Docker**: This app is Docker-ready, which allows you to run the app inside a container.

## 🏗️ How It Works

1. **Start FastAPI**: When you run this app, FastAPI will listen for incoming HTTP requests.
2. **Connect to MongoDB**: The app interacts with MongoDB to store and retrieve data as needed.
3. **Handle File Storage**: If you need to store files, it connects to **MinIO**, which stores your files in an object storage bucket.
4. **CORS Middleware**: Allows other domains to access your API, making it easier to build frontend apps that consume your API.

## 🐳 Docker Setup

You can easily run this project using **Docker**. Here's how to do it:

1. Clone the repository.
2. Build the Docker containers:
   ```bash
   docker-compose up --build
   ```
3. Visit the app at `http://localhost:8000`.

Docker ensures that the app runs in an isolated, consistent environment. **No worries about environment mismatches**! 🎉

## 📑 API Documentation

The app comes with **Swagger UI** automatically generated by FastAPI. To view the API documentation:

1. Start the app by running it locally (via Docker or directly).
2. Visit `http://localhost:8000/docs` to explore the API endpoints. 🚀

## 💬 Additional Notes

- **MongoDB** and **MinIO** run in their own Docker containers (if you're using Docker).
- Make sure that your **Docker Compose** file correctly sets up MongoDB and MinIO services.
- You can easily extend this project by adding more API endpoints or integrating more services.

## 💻 Sample Project Structure

```bash
my_project/
│
├── app/
│   ├── main.py              # FastAPI app code
│   ├── models.py            # Pydantic models
│   ├── database.py          # MongoDB integration
│   └── storage.py           # MinIO integration
│
├── Dockerfile               # Docker configuration for the app
├── docker-compose.yml       # Compose configuration for MongoDB and MinIO
└── README.md                # This file!
```

## 🤝 Contributing

We welcome contributions! If you have ideas to improve the project or if you'd like to add new features, feel free to open an issue or a pull request. Let’s make this template even better together! 🌍

## 📜 License

This project is licensed under the [MIT License](LICENSE), which means you can freely use, modify, and distribute the code!

---

Hope this README makes it clear how this FastAPI, MongoDB, and MinIO template works! Happy coding, and have fun building amazing apps! 🚀🎉