FROM ubuntu:14.04

RUN apt-get update && apt-get install -y \
          python3-dev \
          python3-pip \
          git \
          software-properties-common \
          && cd /usr/local/bin \
          && ln -s /usr/bin/python3 python

COPY ./requirements.txt ./face_app.py /app/
WORKDIR /app

RUN pip3 install --upgrade pip 
RUN pip3 install -r requirements.txt

ENV FLASK_APP=face_app.py LC_ALL=C.UTF-8 LANG=C.UTF-8

CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]