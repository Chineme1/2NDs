# Use Python base image instead of Selenium image
FROM python:3.10-slim

# Install Chrome and ChromeDriver
RUN apt-get update && apt-get install -y wget curl gnupg unzip \
    && curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y google-chrome-stable \
    && wget -q https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip -d /usr/local/bin/ \
    && rm chromedriver_linux64.zip

# Set the working directory inside the container
WORKDIR /app

# Copy the application code to the working directory
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask app port
EXPOSE 5000

# Define the environment variable for Flask
ENV FLASK_APP=server.py

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]

# FROM ubuntu:bionic
#FROM python:3.10

#RUN apt-get update && apt-get install -y \
#    fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 \
#    libnspr4 libnss3 lsb-release xdg-utils libxss1 libdbus-glib-1-2 \
#    curl unzip wget vim xvfb libgbm1 libu2f-udev libvulkan1

#RUN CHROMEDRIVER_VERSION=114.0.5735.90 && \
#    wget https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
#    unzip chromedriver_linux64.zip -d /usr/bin && chmod +x /usr/bin/chromedriver && rm chromedriver_linux64.zip

#RUN wget -O google-chrome.deb "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb" && \
#    dpkg -i google-chrome.deb && apt-get install -y -f && rm google-chrome.deb

#ENV LANG C.UTF-8 \
#    LC_ALL C.UTF-8 \
#    PYTHONUNBUFFERED=1 \
#    PATH="$PATH:/bin:/usr/bin"

#WORKDIR /app

#COPY requirements.txt /app
#RUN pip3 install -r requirements.txt

#COPY . /app
#CMD ["python3", "server.py"]
