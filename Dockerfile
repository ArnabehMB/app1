# Use the official Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the Python script into the container
COPY app.py .

# Expose port 80
EXPOSE 80

# Run the Python HTTP server
CMD ["python", "app.py"]
