# Use the official Python image as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Download the SpaCy model
RUN python -m spacy download en_core_web_sm

# Copy the FastAPI application code into the container
COPY . .

# Expose port 
EXPOSE 3000

# Command to run the FastAPI application using Uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]
