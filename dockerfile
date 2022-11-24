# dockerfile 작성자
# MAINTAINER name

FROM python:3

# COPY ./* ./

# RUN apt-get update && \
#    apt-get install nginx -y && \
#    echo "running dockerfile..."

# 이미지 빌드 시 실행되는 명령어
RUN pip install slack_sdk && \
    pip install datetime && \
    pip install random && \
    echo "running dockerfile..."

# Clean up APT when done.
# RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# CMD 명령어가 실행될 경로
WORKDIR ./

# 백그라운드에서 실행하도록
# 이미지에서 파이썬 스크립트를 실행하는 것이므로 컨테이너가 실행될 때 
CMD ["python","chuucar.py"]

# port number
EXPOSE 80
