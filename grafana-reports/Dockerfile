FROM python:3.8-slim

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    unzip \
    wget \
    libxss1 \
    libappindicator1 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip \
    && pip install selenium webdriver_manager

WORKDIR /grafana-reports

RUN mkdir -p /grafana-reports/scripts

# Install Google Chrome
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get install -f ./google-chrome-stable_current_amd64.deb -y \
    && rm google-chrome-stable_current_amd64.deb

# Install ChromeDriver
RUN wget -q https://storage.googleapis.com/chrome-for-testing-public/128.0.6613.119/linux64/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip \
    && rm chromedriver_linux64.zip

# Verify Chrome and ChromeDriver versions
RUN google-chrome --version
RUN chromedriver-linux64/chromedriver --version

# Copy scripts into the container
COPY scripts/ /grafana-reports/scripts/

# Validate copied files
RUN ls -l && pwd 
RUN ls -l scripts

ENTRYPOINT ["/bin/bash", "-c", "/grafana-reports/scripts/daily-reports.sh"]
