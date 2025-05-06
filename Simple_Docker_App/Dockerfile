# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install uvicorn
# Expose port
EXPOSE 8000

# Run the FastAPI server
CMD ["python", "main.py"]
