# Use a slim Python image as the base
FROM python:latest

# Create a working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy your Flask application code
COPY . .

# Run the Flask development server (or your custom command)
CMD ["python" , "app.py"]