import youtube_dl as yt

playLists = [
    'https://www.youtube.com/watch?v=hSBWxhHCeME&list=PLfYC10OqfICxqUhoExjr_zW9_iQXKYyU0',
]

def getYoutubePlaylist(): 

    for playList in playLists:

        with yt.YoutubeDL({}) as ydl: 
            playList_dict = ydl.extract_info(playList, download=False)

            for video in playList_dict['entries']:
                print("{id :", video.get("id"), "title:", video.get("title"),"upload_date:", video.get("upload_date"), "duration:", video.get("duration") // 60, ":", video.get("duration") % 60, "}") 

                def getTime():
                    minutes = video.get("duration") // 60
                    if len(minutes) == 1:
                        minutes = "0" + minutes

                    seconds = video.get("duration")  % 60
                    if len(seconds) == 1:
                        seconds = "0" + seconds

                    return minutes + ":" + seconds

                video_duration  = getTime()

                videoInfo = { 
                    "id"            : video.get("id"), 
                    "title"         : video.get("title"),
                    "upload_date"   : video.get("upload_date"), 
                    # "duration"      : video.get("duration") // 60, ":", video.get("duration") % 60,
                    "duration"      : video_duration,
                }


getYoutubePlaylist()


