# dockers-flask-OriVered
# Multi-Language Code Execution System

This project implements a multi-language code execution system using Docker and Flask. The system consists of four Docker containers that communicate with each other to execute code written in Java, Python, and Dart.

## Table of Contents

- [Setup](#setup)
- [Project Structure](#project-structure)
- [Building and Running the Containers](#building-and-running-the-containers)
- [Client](#client)
## Setup

To run the code execution system, you need to have Docker installed on your local machine. Please refer to the official Docker documentation for installation instructions: [https://docs.docker.com](https://docs.docker.com)

## Project Structure

The project has the following directory structure:

- `router/`: Contains the Flask application for the router.
- `java-executor/`: Contains the Flask application for the Java executor.
- `python-executor/`: Contains the Flask application for the Python executor.
- `dart-executor/`: Contains the Flask application for the Dart executor.

Each directory contains a Dockerfile for building the corresponding Docker image.

## Building and Running the Containers

To build and run the Docker containers for the code execution system, follow these steps:

1. Make sure Docker is running on your machine.
2. Open a terminal and navigate to the project root directory.
3. Run the following command to build the Docker images:

   ```shell
   make build
    ```
   
This command will build the Docker images for the router and the three language executors.

1. After the images are built, run the following command to start the Docker containers:
   ```shell
   make run
    ```
   This command will create and start the Docker containers based on the built images.
2. The containers should now be running, and you can send requests to the code execution system.

## Client

A client application has been implemented using Flask to interact with the code execution system. The client allows you to execute code in different languages and test the functionality of the system.

### Setup

To set up and run the client application, follow these steps:

1. Open a terminal and navigate to the `client/` directory.
2. Install the required dependencies by running the following command:

   ```shell
   pip install -r requirements.txt
    ```
   
Running the Client
To run the client application, execute the following command in the client/ directory:
   ```shell
   python app.py
   ```
   
The client application will start, and you can access it in your web browser at 
http://localhost:6000.
