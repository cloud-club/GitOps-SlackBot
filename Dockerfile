FROM python:3.8-alpine

WORKDIR /root

ADD . .

RUN pip install --upgrade pip && \
    pip install slack_sdk && \
    pip install datetime

CMD ["python","chuucar.py"]