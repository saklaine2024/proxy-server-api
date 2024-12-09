# Use the Python 3.10 slim image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only the requirements file first to leverage Docker cache for faster builds
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port that your application will run on (optional, if your app listens on a specific port)
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
