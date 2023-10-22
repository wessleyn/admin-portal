# Use the base Python image with the specified version
FROM python:3.12.0-slim as base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the application code into the container
COPY . .

# Install the Python dependencies from requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    pip install -r requirements.txt

# Expose port 8000 for the Django server
EXPOSE 8000

# Start the Django development server
CMD python manage.py runserver 0.0.0.0:8000
