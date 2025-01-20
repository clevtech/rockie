# This file is for standard FastAPI app
from fastapi import FastAPI, HTTPException, Query, Path, Request
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, timezone
from pymongo import MongoClient, errors
from bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html
import os
import requests
from minio import Minio
from minio.error import S3Error
from io import BytesIO
from pymongo import DESCENDING


# MongoDB configuration
MONGO_URI = os.getenv('MONGODB', "mongodb://clevtech:clevtech@mongodb:27017/")
mongo_client = MongoClient(MONGO_URI)
db = mongo_client["my_db"]
collection = db["my_collection"]

# MinIO Setup
minio_client = Minio(
    "minio:9000",
    access_key="clevtech",
    secret_key="clevtech",
    secure=False
)

BUCKET_NAME = "files"

# Ensure the bucket exists
try:
    if not minio_client.bucket_exists(BUCKET_NAME):
        minio_client.make_bucket(BUCKET_NAME)
except S3Error as e:
    print(f"Error checking bucket: {e}")

## FastAPI application
app = FastAPI(title="My app", root_path="/my_app")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,  # Allow cookies and authentication headers
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}