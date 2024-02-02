FROM soflane/transmission-watch-folders
#LABEL maintainer="dev@soflane.ovh"
#LABEL url="https://github.com/soflane"

ENV RPC_WATCH_TV_FOLDER=/torrents/TV
ENV RPC_WATCH_MOVIES_FOLDER=/torrents/Movies
ENV RPC_WATCH_VR_FOLDER=/torrents/VR
ENV RPC_WATCH_OTHER_FOLDER=/torrents/Other
ENV RPC_CLIENT_HOST=transmission
ENV RPC_CLIENT_PORT=9091

ADD root/ /
