# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.


ARG PYTHON_VERSION=3.10
FROM python:${PYTHON_VERSION} AS base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

# specify the directory from which subsequent commands run
WORKDIR /app

# copy requirements.txt to working directory
COPY requirements.txt ./

# Install necessary dependencies from the requirements.txt.
RUN pip install -r requirements.txt

# Copy the source code into the container.
COPY . .

# Expose the port that the application listens on.
EXPOSE 8000

# Run the application.
# CMD ["gunicorn", "messaging_app.wsgi", "--bind=0.0.0.0:8000"]
CMD ["./manage.py", "runserver", "0.0.0.0:8000"]
