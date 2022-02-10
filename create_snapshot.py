import time
import datetime
from PIL import ImageGrab
import os
import shutil
import json
import webbrowser

dirName = 'Flutter Widget of the Week'
# dirName = 'New to Figma Get started with Figma for beginners tutorials'

def createOutDir(name): 
    path = dirName + "/" + name
    if os.path.isdir(path):
        pass
        # shutil.rmtree(path)
    os.makedirs(path) 

def screenShot(fileName):
    bbox= (80, 200, 1400, 1020)
    screenshot = ImageGrab.grab(bbox=bbox)
    screenshot.save(fileName)

def snapshotLoop(interval, duration, name):
    for num in range((duration // interval) -6):
        time.sleep(interval)

        now = datetime.datetime.now()
        print(num, " : ", now)

        fileName  = dirName 
        fileName += '/'
        fileName += name
        fileName += '/'
        fileName += name
        fileName += '_'
        fileName += now.strftime('%Y-%m-%d_%H-%M-%S')
        fileName += '.png'

        screenShot(fileName)

def playYoutube(videoId):
    url = 'https://youtu.be/' + videoId
    webbrowser.open(url)

def loadYoutubePlayListJson():
    # jsonFileName = 'youtube_playlist.json'
    jsonFileName = dirName + '.json'
    with open(jsonFileName,"r") as f:
        json_string = json.load(f)
    return json_string

youtubePlayList = loadYoutubePlayListJson()

def createScreenshot():
    interval = 3

    for videoInfo in youtubePlayList:
        id = videoInfo["id"]
        name = videoInfo["shortTitle"]
        duration = videoInfo["duration"]

        createOutDir(name)
        playYoutube(id)
        time.sleep(4)
        snapshotLoop(interval, duration, name)

createScreenshot()
