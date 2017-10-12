FROM python:2.7
ADD . /todo
WORKDIR /todo
RUN pip install -r requirements.txt
ENV SECRET_KEY = 'this_is_the_secret_key'