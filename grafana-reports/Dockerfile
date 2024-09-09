FROM python:3.8-slim
SHELL [ "/bin/bash", "-c" ]

RUN apt-get update && apt-get install -y \
    fonts-liberation \
    unzip \
    wget \
    libxss1 \
    libappindicator1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatspi2.0-0 \
    libcurl3-gnutls \
    libcurl3-nss \
    libcurl4 \
    libdrm2 \
    libgbm1 \
    libgtk-3-0 \
    libgtk-4-1 \
    libnspr4 \
    libnss3 \
    libvulkan1 \
    libxkbcommon0 \
    xdg-utils \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip \
    && pip install selenium webdriver_manager pyyaml

WORKDIR /grafana-reports

RUN mkdir -p /grafana-reports/scripts

# Install Google Chrome
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get install -f ./google-chrome-stable_current_amd64.deb -y \
    && rm google-chrome-stable_current_amd64.deb
RUN google-chrome --version

# Install ChromeDriver
RUN wget -q https://storage.googleapis.com/chrome-for-testing-public/128.0.6613.119/linux64/chromedriver-linux64.zip \
    && unzip chromedriver-linux64.zip \
    && rm chromedriver-linux64.zip

# Verify Chrome and ChromeDriver versions
RUN google-chrome --version
RUN chromedriver-linux64/chromedriver --version

# Copy scripts into the container
COPY scripts/ /grafana-reports/scripts/

# Validate copied files
RUN ls -l && pwd 
RUN ls -l scripts

ENTRYPOINT ["/bin/bash", "-c", "/grafana-reports/scripts/daily-reports.sh"]