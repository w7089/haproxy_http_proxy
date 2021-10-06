FROM python:3.9

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY client.py .

CMD python3 client.py