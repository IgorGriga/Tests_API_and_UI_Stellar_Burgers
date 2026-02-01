#FROM mcr.microsoft.com/playwright/python:v1.47.0-noble
#
#WORKDIR /usr/workspace
#
#RUN apt-get update && apt-get install -y \
#    gcc \
#    && rm -rf /var/lib/apt/lists/*
#
#COPY requirements.txt .
#RUN pip install --no-cache-dir -r requirements.txt
#RUN playwright install --with-deps
#
#COPY . .
#
#CMD ["pytest", "tests/"]


FROM mcr.microsoft.com/playwright/python:v1.47.0-noble

WORKDIR /usr/workspace

RUN apt-get update && \
    apt-get install -y gcc openjdk-17-jre nodejs npm && \
    export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64 && \
    export PATH=\$JAVA_HOME/bin:\$PATH && \
    npm install -g allure-commandline --save-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install --with-deps chromium firefox webkit

COPY . .

ENV BROWSER=chromium
ENV MARKER=smoke
ENV THREADS=1

CMD ["/bin/sh", "-c", "pytest tests/"]
