# Use an official Selenium image with Chrome and ChromeDriver
FROM selenium/standalone-chrome:latest

# Set the working directory inside the container
WORKDIR /app

# Install Python and other dependencies needed for Flask
RUN sudo apt-get update && \
    sudo apt-get install -y python3 python3-pip

# Copy the application code to the working directory in the container
COPY . /app

# Install Python dependencies, including Flask and Selenium
RUN pip3 install --no-cache-dir -r requirements.txt --break-system-packages

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
