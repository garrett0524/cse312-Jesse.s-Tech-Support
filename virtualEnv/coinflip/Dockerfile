# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files to the working directory
COPY . .

# Expose the port on which the Django app will run (default is 8000)
EXPOSE 8080

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]