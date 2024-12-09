# Use a specific version of the Python 3.10 slim image as base
FROM python:3.10-slim

# Set environment variables to optimize Python behavior in Docker
# - PYTHONUNBUFFERED: Ensures that Python output is not buffered, useful for logging
# - PIP_NO_CACHE_DIR: Ensures no pip cache is saved, reducing image size
ENV PYTHONUNBUFFERED 1
ENV PIP_NO_CACHE_DIR=off

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the requirements file to the container to leverage Docker's cache layer for faster builds
COPY requirements.txt .

# Install dependencies listed in requirements.txt
# Use --no-cache-dir to avoid saving installation caches, reducing image size
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port that your app will run on (optional)
# This should match the port that your app listens to (in your case, port 5000)
EXPOSE 5000

# Define the default command to run your app
# In this case, we are running a Python script named "app.py"
CMD ["python", "app.py"]
