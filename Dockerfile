FROM python:3.9

COPY requirements.txt requirements.txt

RUN apt-get update && python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /usr/src/bot

RUN mkdir -p /usr/src/bot
WORKDIR /usr/src/bot


CMD ["python3","main.py"]