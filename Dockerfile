# Use a minimal Python base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application files to the container
COPY . /app

# Ensure the data file exists (if not, initialize it, first load fill it)
RUN echo '{"service_a": "on", "service_b": "on"}' > /app/data.json

# Expose the port the app listens on
EXPOSE 5000

# Command to run the Python application
CMD ["python", "app.py"]
