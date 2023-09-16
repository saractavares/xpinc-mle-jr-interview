# Use the official Python image as the base image
FROM python:3.11-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the project files to the container
COPY . .

# Install project dependencies
RUN pip install -r requirements.txt

# Expose the port that the application will run on
EXPOSE 8080

# Command to run the application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

