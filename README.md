# WORK IN PROGRESS
This is only theorical for the moment, the plan is to dockerize this little tool to be able to add as addon in a media docker stack (and sync the watchfolders with a cloud storage for my personal 	example)

## Transmission Watch Folders

A small Python script which provides a way to automate multiple watch directories when using `TransmissionRPC`, an API version of the popular Transmission torrent client. This should work remotly as the torrent is send as base64 encoded file throught the API. 

The script runs in the background and searches the specified watch directories for torrent files, every 1 minute by default.




#### Working with environment variables 
| Variable                   | Use                                         |    Default value |
| -------------------------- | :------------------------------------------ | ---------------: |
| RPC_WATCH_TV_FOLDER        | Folder to watch .torrent files (TV shows)   |     /torrents/TV |
| RPC_WATCH_MOVIES_FOLDER    | Folder to watch .torrent files (Movies)     | /torrents/Movies |
| RPC_WATCH_TV_FOLDER        | Folder to watch .torrent files (Music)      |  /torrents/Music |
| RPC_DOWNLOAD_TV_FOLDER     | Where Transmission should download TV shows |                  |
| RPC_DOWNLOAD_MOVIES_FOLDER | Where Transmission should download Movies   |                  |
| RPC_DOWNLOAD_MUSIC_FOLDER  | Where Transmission should download Music    |                  |
| RPC_CLIENT_HOST            | Transmission Web UI host                    |      transmision |
| RPC_CLIENT_PORT            | Transmission Web UI port                    |             9091 |
| RPC_CLIENT_USER            | Transmission Web UI username                |                  |
| RPC_CLIENT_PASSWORD        | Transmission Web UI password                |                  |
####  Logs

For now, the logs will come in this folder so feel free to make a volume. 
It is not my priority, but best would be to access it via docker logs also 

/opt/logs



### Getting Started

#### Prerequisites
* `Docker`
* `Transmission`

#### Installing

#### Configuration


#### Adding Or Removing Directories
Because this is a pretty quick-and-dirty solution, there is only 3 watchfolders. But as open source is open, don't hesitate to pull requests. 


#### Other Notes
Tested on Ubuntu Server 16.04 LTS.
