FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install curl
RUN apt-get update && apt-get install -y curl git && rm -rf /var/lib/apt/lists/*

# Create the destination directory
RUN mkdir -p /root/.cache/torch/hub

# Clone the repo into the desired folder
RUN git clone https://github.com/WongKinYiu/yolov9.git /root/.cache/torch/hub/yolov9-main

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app ./app

# Expose port
EXPOSE 8000

# Run API server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

