FROM portus.in.chaitin.net/x-ray-public/python:3.6-slim AS build
RUN sed -i 's|deb.debian.org|mirrors.tuna.tsinghua.edu.cn|g' /etc/apt/sources.list && \
    sed -i 's|security.debian.org|mirrors.tuna.tsinghua.edu.cn/debian-security|g' /etc/apt/sources.list && \
WORKDIR /web/
COPY ../../../* .
RUN pip install  -r requirements.txt

