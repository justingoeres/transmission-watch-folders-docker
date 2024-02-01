#!/usr/bin/python

import time
import os, sys, linecache
import os.path as path
import transmissionrpc
import datetime
import base64

# Watch directories
watch_tv = os.environ['RPC_WATCH_TV_FOLDER']
watch_movie = os.environ['RPC_WATCH_MOVIES_FOLDER']
watch_vr = os.environ['RPC_WATCH_VR_FOLDER']
watch_other = os.environ['RPC_WATCH_OTHER_FOLDER']

# Complete download directories
download_dir_tv = os.environ['RPC_DOWNLOAD_TV_FOLDER']
download_dir_movie = os.environ['RPC_DOWNLOAD_MOVIES_FOLDER']
download_dir_vr = os.environ['RPC_DOWNLOAD_VR_FOLDER']
download_dir_other = os.environ['RPC_DOWNLOAD_OTHER_FOLDER']
 
client = transmissionrpc.Client(
    address=os.environ['RPC_CLIENT_HOST'],
    port=os.environ['RPC_CLIENT_PORT'],
    user=os.environ['RPC_CLIENT_USER'],
    password=os.environ['RPC_CLIENT_PASSWORD']
    )

# Logging
log = open('/var/log/python-rpc-folders.txt', 'a')
timestamp = '[{:%Y-%m-%d %H:%M:%S}]'.format(datetime.datetime.now())
print(timestamp +  ' ' + 'Started watch script.', file=log)
print('Current watch directories:', file=log)
print('    TV: ' + watch_tv, file=log)
print('Movies: ' + watch_movie, file=log)
print(' VR: ' + watch_vr, file=log)
print(' Other: ' + watch_other, file=log)
print('Current download directories:', file=log)
print('    TV: ' + download_dir_tv, file=log)
print('Movies: ' + download_dir_movie, file=log)
print(' VR: ' + download_dir_vr, file=log)
print(' Other: ' + download_dir_other, file=log)
log.close()


#Print the exception handling with the line number 
def PrintException(logfile):
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print ('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj),file=logfile)


def add(watch_dir, download_dir):
    for entry in os.scandir(watch_dir):
        if entry.name.lower().endswith('.torrent') and entry.is_file():
            log = open('/var/log/python-rpc-folders.txt', 'a')
            timestamp = '[{:%Y-%m-%d %H:%M:%S}]'.format(datetime.datetime.now())
            try:
                print(timestamp + ' ' + 'Adding torrent: ' + entry.name, file=log)
                with open(watch_dir + '/' + entry.name, "rb") as f:
                    encoded = base64.b64encode(f.read()).decode('utf-8')
                newTorrent = client.add_torrent(encoded, download_dir=download_dir)
                time.sleep(1)
                newTorrent.start()
                os.remove(watch_dir + '/' + entry.name)
            except Exception as e:
                print(timestamp + ' ' + 'Error encountered for directory ('+ watch_dir + ') : ' + str(e), file=log)
                PrintException(log)
            log.close()
            time.sleep(1)
        else: 
            log = open('/var/log/python-rpc-folders.txt', 'a')
            timestamp = '[{:%Y-%m-%d %H:%M:%S}]'.format(datetime.datetime.now())
            print(timestamp + ' ' + 'No torrent file found for directory ('+ watch_dir + ') : ' + entry.name, file=log)
            

while True:
    log = open('/var/log/python-rpc-folders.txt', 'a')
    timestamp = '[{:%Y-%m-%d %H:%M:%S}]'.format(datetime.datetime.now())
    print(timestamp + ' ' + 'Searching directories.', file=log)
    add(watch_tv, download_dir_tv)
    add(watch_movie, download_dir_movie)
    add(watch_vr, download_dir_vr)
    add(watch_other, download_dir_other)
    log.close()
    time.sleep(30)
