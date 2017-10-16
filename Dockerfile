FROM python:latest
ADD . /dm
WORKDIR /dm
RUN apt-get update && apt-get install -y \
    sudo
RUN pip install -r requirements.txt
ENV SECRET_KEY = 'this_is_the_secret_key'