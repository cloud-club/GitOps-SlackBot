# # FROM 이미지 이름:태그명
# FROM python3

# # dockerfile 작성자
# MAINTAINER yugyeong <uugyeong27@gmail.com>

# # Clean up APT when done.
# RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# EXPOSE 80

# CMD  echo "dockerfile test"

FROM python:3

RUN apt update && \
    apt install nginx -y

COPY ./* ./

CMD ["python","chuucar.py"]