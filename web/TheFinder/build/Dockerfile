FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FLAG="defensys{ormagadon_the_finder_of_bugs}"

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Copy the start.sh script and make it executable
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

# Run the start.sh script
CMD ["bash", "/app/start.sh"]