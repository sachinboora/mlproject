FROM python:3.12.2-slim-bullseye 
WORKDIR /app
COPY . /app

RUN apt update -y && apt install awscli -y

RUN pip3 install -r  requirements.txt
CMD ["python3", "application.py"]