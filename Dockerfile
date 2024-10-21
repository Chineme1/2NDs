FROM python:3.11-slim

# Install required packages
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    libxi6 \
    libgconf-2-4 \
    libnss3 \
    libasound2 \
    libx11-xcb1 \
    fonts-liberation \
    && apt-get clean

# Install Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y google-chrome-stable

# Install your Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy your application code
COPY . .

# Expose the port
EXPOSE 5000

# Run your application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "server:app"]
