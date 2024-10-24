# Use Python base image instead of Selenium image
FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN apt-get update && apt-get install -y wget unzip && \
  wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
  apt install -y ./google-chrome-stable_current_amd64.deb && \
  rm google-chrome-stable_current_amd64.deb && \
  apt-get clean


CMD ["python", "server.py"]


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
