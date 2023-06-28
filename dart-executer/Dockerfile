# Use your local Python version as a parent image
FROM python:3.7.4-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install required packages
RUN apk add --no-cache bash curl gnupg

# Import the signing key
RUN curl https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --import

# Install Dart SDK
RUN curl https://storage.googleapis.com/dart-archive/channels/stable/release/latest/sdk/dartsdk-linux-x64-release.zip -o dartsdk.zip
RUN unzip dartsdk.zip -d /usr/lib
RUN rm dartsdk.zip
ENV PATH $PATH:/usr/lib/dart-sdk/bin

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5003 available to the world outside this container
EXPOSE 5003

# Run the application when the container launches
CMD ["python", "dart-executer.py"]
