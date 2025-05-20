# Use a Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the application files into the container
COPY . /app/

# Expose the application port
EXPOSE 5000

# Set the default command to run the app
CMD ["python", "app.py"]
