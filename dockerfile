# dockerfile 작성자
# MAINTAINER name

FROM python:3

# COPY ./* ./

RUN apt-get update && \
    apt-get install nginx -y && \
    echo "running dockerfile..."

# Clean up APT when done.
# RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# CMD 명령어가 실행될 경로
WORKDIR .

# 백그라운드에서 실행하도록
CMD ["python","chuucar.py"]

# port number
EXPOSE 80