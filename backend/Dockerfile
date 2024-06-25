# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install PostgreSQL client tools
RUN apt-get update && \
    apt-get install -y postgresql-client

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy just the requirements file first to leverage Docker caching
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the script as executable
RUN chmod +x /usr/src/app/entrypoint.sh

EXPOSE 8000
