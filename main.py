import pyautogui
import time
import datetime
from PIL import ImageGrab
import os
import shutil
import youtube_dl as yt
import pprint

name = 'FadeInImage'
name = 'path_provider'
playLists = [
    # 'https://www.youtube.com/watch?v=8ZaFk0yvNlI&list=PLjxrf2q8roU23XGwz3Km7sQZFTdB996iG',
    'https://www.youtube.com/watch?v=hSBWxhHCeME&list=PLfYC10OqfICxqUhoExjr_zW9_iQXKYyU0',
]

sec = 60 * 3
interval = 3

def screen_shot_pil(fileName):
    bbox= (80, 200, 1400, 1020)

    ss = ImageGrab.grab(bbox=bbox)
    ss.save(fileName)

def outDir(): 
    if os.path.isdir(name):
        shutil.rmtree(name)
    os.makedirs(name) 

def screen_shot(fileName):
    region = (100, 100, 500, 500)

    ss = pyautogui.screenshot()
    ss.save(fileName)

def duration():
    for num in range(sec):
        time.sleep(interval)

        now = datetime.datetime.now()
        print(num, " : ", now)

        dirName   = 'widgets'
        fileName  = dirName 
        fileName += '/'
        fileName += name
        fileName += '/'
        fileName += name
        fileName += '_'
        fileName += now.strftime('%Y-%m-%d_%H-%M-%S')
        fileName += '.png'

        screen_shot_pil(fileName)

def getYoutubePlaylist(): 
    # youtube-dl -j --flat-playlist url
    # print(dir(youtube_dl))
    # print(dir(yt.YoutubeDL))
    # youtube_dl.YoutubeDL().download([url])
    # help(yt)

    for playList in playLists:
        # print(playList)
        with yt.YoutubeDL({}) as ydl: 
            playList_dict = ydl.extract_info(playList, download=False)
            # print(playList_dict)

            counter = 0
            for video in playList_dict['entries']:
                # print(video)

                # for prop in ["thumbnail", "id", "title", "description", "duration"]:
                # print("{id :", video.get("id"), "title:", video.get("title"), "duration:", video.get("duration"),"upload_date:", video.get("upload_date"),"}") 
                print("{id :", video.get("id"), "title:", video.get("title"),"upload_date:", video.get("upload_date"), "duration:", video.get("duration") // 60, ":", video.get("duration") % 60, "}") 

                # if counter == 0:
                    # pprint.pprint(video, width=40)

                # counter+=1

def main():
    getYoutubePlaylist()
    # outDir()
    # duration()

main()
