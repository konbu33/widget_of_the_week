import youtube_dl as yt
import pprint
import json
import os 
import re
 

playLists = [
    'https://www.youtube.com/watch?v=8ZaFk0yvNlI&list=PLjxrf2q8roU23XGwz3Km7sQZFTdB996iG',
    # 'https://www.youtube.com/watch?v=Cx2dkpBxst8&list=PLXDU_eVOJTx7QHLShNqIXL1Cgbxj7HlN4',
]

class Video:
    def __init__(self, id, title, upload_date, duration):
        self.id = id
        self.title = title
        self.shortTitle = self.__shortTitle(self.title)
        self.upload_date = upload_date
        self.uploadDate = self.__formatUploadDate(self.upload_date)
        self.duration = duration 
        self.time = self.__sec2minuts(self.duration)

    def __shortTitle(self, title):
        endpoint = title.find(" (")
        shortTitle = title[0:endpoint]
        return shortTitle

    def __sec2minuts(self, duration):

        minutes = duration // 60
        if bool(len(str(minutes)) == 1):
            minutes = "0" + str(minutes)

        seconds = duration % 60
        if bool(len(str(seconds)) == 1):
            seconds = "0" + str(seconds)

        return str(minutes) + ":" + str(seconds)

    def __formatUploadDate(self, upload_date):
        year  = upload_date[0:4]
        month = upload_date[4:6]
        day   = upload_date[6:8]

        return year + "/" + month + "/" + day

youtubePlaylist = []


def getYoutubePlaylist(): 

    for playList in playLists:

        with yt.YoutubeDL({}) as ydl: 
            playList_dict = ydl.extract_info(playList, download=False)
            # pprint.pprint(playList_dict)
            playlistTitle = playList_dict['title']
            playlistTitle = re.sub('"',"",playlistTitle) 
            playlistTitle = re.sub('\?',"",playlistTitle) 
            print('playlistTitle : ', playlistTitle)

            for video in playList_dict['entries']:
                videoInfo = Video(video.get("id"), video.get("title"), video.get("upload_date"), video.get("duration"))
                # print("{id :", videoInfo.id, "title:", videoInfo.title, "upload_date:", videoInfo.uploadDate, "duration:", videoInfo.duration , "time:", videoInfo.time, "}") 
                # print(dir(video))

                youtubePlaylist.append(videoInfo)
            
            return playlistTitle


def outJsonFile():
    # outFileName = 'youtube_playlist.json'
    outFileName = playlistTitle + ".json"
    print('playlistTitle : ', playlistTitle)

    print(outFileName)
    if os.path.isfile(outFileName):
        os.remove(outFileName)

    with open(outFileName,"a", newline='\n') as f:
        json.dump([ob.__dict__ for ob in youtubePlaylist],f,ensure_ascii=False, indent=1)

playlistTitle = getYoutubePlaylist()
outJsonFile()

   

