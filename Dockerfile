# Use Python base image
FROM python:3.12

# Install wkhtmltopdf
RUN apt-get update && apt-get install -y wkhtmltopdf

# Set working directory
WORKDIR /app

# Copy app files
COPY . .

EXPOSE 5000

# Install dependencies
# Keeps the image lightweight by preventing package 
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt


# Run Flask app
CMD ["python", "app.py"]