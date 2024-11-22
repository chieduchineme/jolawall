# Use the Python 3.11 image
FROM python:3.11.4-slim

# Set the working directory in the container
WORKDIR /AiGuard

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . /AiGuard

# Expose port 50052 for gRPC
EXPOSE 50052

# Run the Django application with grpcrunserver on port 50052
CMD ["python", "manage.py", "grpcrunserver"]