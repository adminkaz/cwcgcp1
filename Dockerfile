FROM python:3.9
ENV PYTHONNUMBERFUFFERED 1
#RUN apt install -y python3-pip
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get install libpq-dev
RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "vim"]
RUN pip install -r requirements.txt
COPY . /code/
