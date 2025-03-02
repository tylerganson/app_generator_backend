# Use Python as the base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy all files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 for Google Cloud Run
EXPOSE 8080

# Start the server using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "server:app"]
