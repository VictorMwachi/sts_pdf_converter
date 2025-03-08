# Use Python base image
FROM python:3.12

# Install wkhtmltopdf

RUN wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.focal_amd64.deb
RUN apt install ./wkhtmltox_0.12.6-1.focal_amd64.deb

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