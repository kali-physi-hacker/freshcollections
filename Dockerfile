# Pull base image
FROM python:3.8

# SET DOCKER ENVIRONMENTS VARIABLES FOR FLAGGING
ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# SET A WORKING DIRECTORY IN DOCKER IMAGE WORKSPACE
WORKDIR /estore

# Project Requirements installation
COPY requirements.base /estore/
COPY requirements.prod /estore/
RUN pip install -r requirements.base
RUN pip install -r requirements.prod

# COPY MAIN PROJECT TO DOCKER IMAGE WORKSPACE
COPY . /estore/