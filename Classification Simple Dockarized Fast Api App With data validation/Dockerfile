# Use Python base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy files
COPY ./app ./app
COPY ./model ./model
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the app
CMD ["python","-m","app.main"]

