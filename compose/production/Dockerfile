FROM python:3.11.4-slim-buster


ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Install system dependencies
RUN apt-get update &&  \
    apt-get install -y netcat && \
    apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip and install Python dependencies
COPY ./requirements/production.txt ./requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

WORKDIR /app

COPY ./app /app

COPY ./scripts /scripts

EXPOSE 80

# Make scripts executable and fix potential issues with line endings on different OSs
RUN sed -i 's/\r$//g' /scripts/run && \
    chmod +x /scripts/run && \
    sed -i 's/\r$//g' /scripts/start-celerybeat && \
    chmod +x /scripts/start-celerybeat && \
    sed -i 's/\r$//g' /scripts/start-celeryworker && \
    chmod +x /scripts/start-celeryworker && \
    sed -i 's/\r$//g' /scripts/start-flower && \
    chmod +x /scripts/start-flower