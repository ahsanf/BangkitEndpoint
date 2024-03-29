# Use the official lightweight Python image.     
# https://hub.docker.com/_/python
FROM python:3.9-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN pip3 install --upgrade setuptools pip
RUN pip3 install Flask gunicorn
RUN pip3 install pyzoom
RUN pip3 install tensorflow
RUN pip3 install opencv-python
RUN pip3 install fer
RUN pip3 install numpy
RUN pip3 install mtcnn
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y


# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main_v1:app