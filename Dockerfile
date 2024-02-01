FROM python:3.6-alpine
#LABEL maintainer="dev@soflane.ovh"
#LABEL url="https://github.com/soflane"

ARG S6_OVERLAY_VERSION=3.1.6.2

ENV RPC_WATCH_TV_FOLDER=/torrents/TV
ENV RPC_WATCH_MOVIES_FOLDER=/torrents/Movies
ENV RPC_WATCH_VR_FOLDER=/torrents/VR
ENV RPC_WATCH_OTHER_FOLDER=/torrents/Other
ENV RPC_CLIENT_HOST=transmission
ENV RPC_CLIENT_PORT=9091

ADD https://github.com/just-containers/s6-overlay/releases/download/v${S6_OVERLAY_VERSION}/s6-overlay-noarch.tar.xz /tmp
ADD https://github.com/just-containers/s6-overlay/releases/download/v${S6_OVERLAY_VERSION}/s6-overlay-x86_64.tar.xz /tmp
RUN apk update \
    && apk add py-pip \
    && pip install transmissionrpc \
    && tar -C / -Jxpf /tmp/s6-overlay-noarch.tar.xz \
    && tar -C / -Jxpf /tmp/s6-overlay-x86_64.tar.xz \
    && rm -rf /tmp \
    && rm -rf /var/lib/apt/lists/* 
ADD root/ /

ENTRYPOINT ["/init"]
CMD python /app/main.py



