from xml.dom import VALIDATION_ERR
import pytube
from pytube import exceptions
import os


path="D:"

while True:
    url = input('Copy and paste video url here>:')
    try:
        yt  =pytube.YouTube(url)
    except VALIDATION_ERR:
        print('video unavailable')
        break
    except exceptions.PytubeError:
        print('pytube error')
        break
    except  exceptions.VideoPrivate:
        print('video is private')
        break
    except exceptions.VideoUnavailable:
        print('video unavailable')
        break       
    else:
        print('Downloading please wait....')
        yt.streams.get_highest_resolution().download(path)
        print('video downloaded in D drive')
    
print("please contact suchith doveloper")