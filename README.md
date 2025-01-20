# 🚀 FastAPI + MongoDB + MinIO + ML Service with Docker Compose

Welcome to the **Dockerized Full-Stack FastAPI Project**! This template provides a backend API powered by **FastAPI**, **MongoDB**, **MinIO**, and **Machine Learning** services, all integrated and easily deployed with Docker Compose. This setup is perfect for developers looking to get started with Docker, FastAPI, MongoDB, MinIO, and GPU-based machine learning.

Let’s walk through how this application works and how to get it up and running! 😎

---

To prepare your **Ubuntu 22.04** system with all necessary tools like **NVIDIA drivers**, **CUDA**, **Docker** (with NVIDIA runtime support), **OpenSSH server**, and **Git**, follow these detailed instructions.

---

## 🌍 **Step 1: Install NVIDIA Drivers**

### 1. **Install NVIDIA Driver on Ubuntu 22.04**

The first step is to install the NVIDIA driver, which is required for running GPU-based tasks. Follow the official guide to install the NVIDIA drivers for your GPU model:

- **Official NVIDIA Driver Installation Guide for Ubuntu**: [NVIDIA Installation Guide](https://www.nvidia.com/en-us/drivers/unix/)
  
Here’s a simple way to install the drivers:

1. **Update your system**:
    ```bash
    sudo apt update
    sudo apt upgrade
    ```

2. **Install the necessary dependencies**:
    ```bash
    sudo apt install build-essential dkms
    ```

3. **Add the NVIDIA PPA and install the latest driver**:
    ```bash
    sudo apt install nvidia-driver-525
    ```

4. **Reboot the system**:
    ```bash
    sudo reboot
    ```

5. **Verify installation**:
    After reboot, you can check if the NVIDIA driver is working by running:
    ```bash
    nvidia-smi
    ```

---

## 🌍 **Step 2: Install CUDA**

CUDA is the NVIDIA platform and programming model for parallel computing, enabling you to leverage GPU resources for your applications.

### 1. **Install CUDA on Ubuntu 22.04**

Follow the official CUDA installation guide: [CUDA Installation Guide for Ubuntu](https://developer.nvidia.com/cuda-downloads)

Here’s how you can do it manually:

1. **Download the CUDA Toolkit**:
   - Visit the [CUDA Downloads page](https://developer.nvidia.com/cuda-toolkit) and select your Ubuntu version.
   - Download and install the appropriate CUDA version.

2. **Install the CUDA package**:
    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

3. **Set up environment variables**:
    Add the following lines to the `.bashrc` file to set the CUDA path:
    ```bash
    echo 'export PATH=/usr/local/cuda-11.7/bin:$PATH' >> ~/.bashrc
    echo 'export LD_LIBRARY_PATH=/usr/local/cuda-11.7/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
    source ~/.bashrc
    ```

4. **Reboot your machine**:
    ```bash
    sudo reboot
    ```

5. **Verify CUDA installation**:
    Run the following command to check if CUDA is installed properly:
    ```bash
    nvcc --version
    ```

---

## 🌍 **Step 3: Install Docker and NVIDIA Docker Toolkit**

### 1. **Install Docker Engine**

Follow the official Docker installation guide: [Docker Engine Installation Guide for Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

1. **Update the apt package list**:
    ```bash
    sudo apt update
    ```

2. **Install Docker dependencies**:
    ```bash
    sudo apt install apt-transport-https ca-certificates curl software-properties-common
    ```

3. **Add Docker’s official GPG key**:
    ```bash
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    ```

4. **Set up the stable Docker repository**:
    ```bash
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    ```

5. **Install Docker**:
    ```bash
    sudo apt update
    sudo apt install docker-ce
    ```

6. **Enable and start Docker**:
    ```bash
    sudo systemctl enable docker
    sudo systemctl start docker
    ```

7. **Verify Docker installation**:
    Run:
    ```bash
    sudo docker --version
    ```

---

### 2. **Install NVIDIA Docker Toolkit**

This allows Docker to utilize your NVIDIA GPU for running containers.

1. **Add the NVIDIA package repository**:
    ```bash
    sudo mkdir -p /etc/systemd/system/docker.service.d
    sudo tee /etc/systemd/system/docker.service.d/override.conf <<EOF
    [Service]
    ExecStart=
    ExecStart=/usr/bin/dockerd --host=fd:// --add-runtime=nvidia=/usr/bin/nvidia-container-runtime
    EOF
    ```

2. **Reload Docker daemon**:
    ```bash
    sudo systemctl daemon-reload
    sudo systemctl restart docker
    ```

3. **Verify NVIDIA Runtime installation**:
    ```bash
    docker run --rm nvidia/cuda:11.7-base nvidia-smi
    ```

---

## 🌍 **Step 4: Install OpenSSH Server**

Install OpenSSH server to enable remote access via SSH:

1. **Install OpenSSH Server**:
    ```bash
    sudo apt install openssh-server
    ```

2. **Enable and start SSH service**:
    ```bash
    sudo systemctl enable ssh
    sudo systemctl start ssh
    ```

3. **Verify SSH status**:
    ```bash
    sudo systemctl status ssh
    ```

4. **Check your IP address**:
    Use `ip a` to find your server’s IP address to connect remotely.

---

## 🌍 **Step 5: Install Git**

Install **Git** to manage version control:

1. **Install Git**:
    ```bash
    sudo apt install git
    ```

2. **Verify Git installation**:
    ```bash
    git --version
    ```

---

## 🌍 **Step 6: Add Local Docker Registry**

To add your **local Docker registry** (e.g., `192.168.1.104:5000`), follow these steps:

### 1. **Configure Docker Daemon to Use Local Registry**

1. **Create or edit the `/etc/docker/daemon.json` file**:
    ```bash
    sudo nano /etc/docker/daemon.json
    ```

2. **Add the following configuration** to allow the local registry and NVIDIA runtime:
    ```json
    {
      "insecure-registries": ["192.168.1.104:5000"],
      "runtimes": {
        "nvidia": "/usr/bin/nvidia-container-runtime"
      }
    }
    ```

3. **Restart Docker** to apply the changes:
    ```bash
    sudo systemctl restart docker
    ```

4. **Verify the changes** by running:
    ```bash
    sudo docker info | grep -i registry
    sudo docker info | grep -i runtime
    ```

---

## 🌍 **Step 7: Verify All Installations**

Finally, verify that everything is installed and configured properly.

1. **Check Docker status**:
    ```bash
    sudo systemctl status docker
    ```

2. **Check NVIDIA GPU status**:
    ```bash
    nvidia-smi
    ```

3. **Check CUDA version**:
    ```bash
    nvcc --version
    ```

4. **Check Docker’s GPU support**:
    ```bash
    docker run --rm nvidia/cuda:11.7-base nvidia-smi
    ```

---

## 📝 **Additional Resources**

1. **NVIDIA Docker Documentation**: [NVIDIA Docker](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)
2. **Docker Documentation**: [Docker Install](https://docs.docker.com/engine/install/ubuntu/)
3. **CUDA Installation Guide**: [CUDA Installation](https://developer.nvidia.com/cuda-downloads)
4. **OpenSSH Server**: [OpenSSH Install](https://help.ubuntu.com/community/SSH/OpenSSHServer)
5. **FastAPI Documentation**: [FastAPI Documentation](https://fastapi.tiangolo.com/)

---

## 🛠️ Services Overview

The Docker Compose file defines the following services:

1. **Backend**: The FastAPI backend service.
2. **MongoDB**: A NoSQL database service for storing and managing data.
3. **Mongo-Express**: A web-based MongoDB admin interface.
4. **Machine Learning (ML)**: A service running machine learning models, possibly leveraging GPU.
5. **MinIO**: Object storage service that’s compatible with Amazon S3, ideal for storing large files like images, videos, etc.

### 1. **Backend Service (FastAPI)**

This service runs the FastAPI backend API, which is responsible for processing HTTP requests.

```yaml
backend:
  image: 192.168.1.104:5000/backend:latest
  build: ./backend
  container_name: backend
  command: uvicorn main:app --host 0.0.0.0 --port 8000 --reload
  restart: always
  ports:
    - "81:8000"
  depends_on:
    - mongodb
  networks:
    - umai_bridge
```

- **Image**: The backend image is built from the `./backend` directory and pushed to a private Docker registry.
- **Command**: The `uvicorn main:app` command runs the FastAPI app on port 8000. The `--reload` flag is used for development, enabling automatic reloads when code changes.
- **Ports**: The backend API is exposed on port `81` (localhost).
- **Dependencies**: It depends on the MongoDB service, ensuring that MongoDB starts first.
  
### 2. **MongoDB Service**

The MongoDB service uses the official MongoDB Docker image. It stores application data.

```yaml
mongodb:
  container_name: mongodb
  logging:
    driver: "none"
  hostname: mongodb
  image: mongo:6.0.6
  networks:
    - umai_bridge
  ports:
    - '27017:27017'
  restart: unless-stopped
  environment:
    - MONGO_INITDB_ROOT_USERNAME=clevtech
    - MONGO_INITDB_ROOT_PASSWORD=clevtech
  volumes:
    - ./volumes/data:/data/db
```

- **Environment**: The `MONGO_INITDB_ROOT_USERNAME` and `MONGO_INITDB_ROOT_PASSWORD` are set to `clevtech` for easy initial setup.
- **Volumes**: Data is stored in the `./volumes/data` directory on the host machine.
- **Ports**: The MongoDB service is accessible on port `27017`.

### 3. **Mongo-Express Service**

This is the admin interface for MongoDB, making it easy to manage your database using a simple web UI.

```yaml
mongo-express:
  image: mongo-express:latest
  container_name: mongo-express
  ports:
    - "8061:8081"
  environment:
    ME_CONFIG_MONGODB_SERVER: mongodb
    ME_CONFIG_MONGODB_ADMINUSERNAME: clevtech
    ME_CONFIG_MONGODB_ADMINPASSWORD: clevtech
    ME_CONFIG_BASICAUTH: true
    ME_CONFIG_BASICAUTH_USERNAME: ml
    ME_CONFIG_BASICAUTH_PASSWORD: clevtech
  depends_on:
    - mongodb
  networks:
    - umai_bridge
```

- **Ports**: Mongo-Express is exposed on port `8061` (localhost).
- **Authentication**: Basic authentication is enabled for Mongo-Express with a username (`ml`) and password (`clevtech`).

### 4. **Machine Learning Service (ML)**

This service runs machine learning models, and it leverages GPU resources if available. It uses FastAPI for serving the models.

```yaml
ml:
  image: 192.168.1.104:5000/recorder:latest
  build: ./ml
  container_name: ml
  command: uvicorn main:app --host 0.0.0.0 --port 8000 --reload
  depends_on:
    - minio
  networks:
    - umai_bridge
  ports:
    - "82:8000"
  restart: always
  deploy:
    resources:
      reservations:
        devices:
          - driver: nvidia
            count: 1
            capabilities: [gpu]
```

- **Ports**: The ML service is exposed on port `82` (localhost).
- **GPU Resources**: If running on a machine with an NVIDIA GPU, this service will reserve 1 GPU device for processing machine learning tasks.

### 5. **MinIO Service**

MinIO is an object storage service for storing files like images, videos, and backups. It provides a compatible API to Amazon S3.

```yaml
minio:
  image: minio/minio:latest
  container_name: minio
  environment:
    MINIO_ROOT_USER: clevtech
    MINIO_ROOT_PASSWORD: clevtech
  command: server /data --console-address ":9090"
  ports:
    - "9000:9000"
    - "9090:9090"
  restart: always
  networks:
    - umai_bridge
  volumes:
    - ./volumes/minio_data:/data
```

- **Ports**: MinIO is accessible on ports `9000` (S3 API) and `9090` (console UI).
- **Volumes**: The storage data is persisted in `./volumes/minio_data`.

---

## 📦 How to Get Started

Follow these steps to launch the entire stack using **Docker Compose**:

### 1. Clone the repository

```bash
git clone https://github.com/clevtech/rockie.git
cd rockie
```

### 2. Build and Start Containers

Use **Docker Compose** to build and start all services:

```bash
docker-compose up --build
```

### 3. Access the Services

- **FastAPI Backend**: Accessible at [http://localhost:81](http://localhost:81)
- **MongoDB**: Running on `mongodb://localhost:27017`
- **Mongo-Express**: Access the MongoDB web admin interface at [http://localhost:8061](http://localhost:8061) (credentials: `ml` / `clevtech`)
- **Machine Learning Service**: Running on [http://localhost:82](http://localhost:82)
- **MinIO Console**: Access at [http://localhost:9090](http://localhost:9090) (credentials: `clevtech` / `clevtech`)

### 4. Stopping the Services

To stop the services, run:

```bash
docker-compose down
```

This will stop and remove the containers but preserve the data in your volumes.

---

## 🔧 Customizing the Configuration

You can modify the environment variables, ports, and other configurations to fit your needs:

- **Backend**: Adjust the backend API or change the exposed ports.
- **MongoDB**: Change the database name or credentials.
- **MinIO**: Configure buckets or S3-compatible settings.
- **Machine Learning**: Add your models or adjust the GPU usage.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve or add new features to this template, feel free to:

1. Fork the repository.
2. Create a new branch for your feature.
3. Make changes and commit them.
4. Open a pull request.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE), which means you're free to use, modify, and share the code! 🎉
