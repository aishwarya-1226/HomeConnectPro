# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . /app/

# Expose port 8000 to be able to access the application
EXPOSE 8000

# Collect static files
#RUN python3 manage.py collectstatic --noinput

# Change ownership and permissions of the static files
#RUN mkdir -p /app/staticfiles && chown -R www-data:www-data /app/staticfiles && chmod -R 755 /app/staticfiles

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
