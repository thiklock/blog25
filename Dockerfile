FROM python:3.11-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1 # Prevents Python from writing .pyc files
ENV PYTHONUNBUFFERED 1       # Prevents Python from buffering stdout/stderr

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    postgresql-client \
    gettext \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

    # Set the working directory
WORKDIR /app
# Set the working directory
WORKDIR /app