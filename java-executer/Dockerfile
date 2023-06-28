# Use an official Python runtime as a parent image
FROM python:3.7.4-alpine

# Add Maintainer Info
LABEL maintainer="email@example.com"

# Set the working directory in the container
WORKDIR /app

# Install OpenJDK
RUN apk add --no-cache openjdk8

# Copy the current directory contents into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5001 available to the world outside this container
EXPOSE 5001

# Run the application when the container launches
CMD ["python", "java-executer.py"]
