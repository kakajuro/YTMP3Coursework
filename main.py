import json
import os
from yt_dlp import YoutubeDL

songInfo = {}
idList = {"list": []}

def downloadSong(URL, startPoint):
    video_info = YoutubeDL().extract_info(url=URL, download=False)
    
    substringsToRemove = ["(Video)", "[Video]", "(Official Video)", "(Official Music Video)", "[Official Video]", "(Music Video)", "[Official Music Video]", "(Official Audio)", "[Official Audio]", "[Music Video]", "(Lyric Video)", "(Official Lyric Video)", "[Lyric Video]", "[Official Lyric Video]"]
    
    substringsToRemove = ["Official", "Video", "Music", "Lyrics", "Lyric", "Lyrics/Lyric", "Audio"]
    
    for substring in substringsToRemove:
      video_info['title'] = video_info['title'].replace(substring, "")
      video_info['title'] = video_info['title'].replace(substring.upper(), "")
      video_info['title'] = video_info['title'].replace(substring.lower(), "")
      
      video_info['title'] = video_info['title'].replace("()", "")
      video_info['title'] = video_info['title'].replace("( )", "")
      video_info['title'] = video_info['title'].replace("(  )", "")
      video_info['title'] = video_info['title'].replace("[  ]", "")
      video_info['title'] = video_info['title'].replace("[ ]", "")
      video_info['title'] = video_info['title'].replace("[]", "")
      video_info['title'] = video_info['title'].replace("(/ )", "")
      print(video_info['title'])

    filename = f"{video_info['id']}|{video_info['title']}"

    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': f'./songs/{filename}.mp3',
        # 'playlist_items': '2'
    }

    songInfo.update({str(video_info["id"]) : [video_info['title'], startPoint]})
    idList["list"].append(video_info["id"])

    with YoutubeDL(options) as ydl:
        ydl.download([URL])


if __name__ == "__main__":
  
    os.makedirs('songs') if not os.path.exists('songs') else None
    
    with open("inputfile.txt", "r") as file:
        lines = file.readlines()
        songNo = len(lines)

        for line in lines:
            try:  
              downloadSong(line.split(",")[0].split("|")[1], line.split(",")[1].strip())
              
              print(f"Download completed: {int(lines.index(line))+1}/{songNo}")
            except Exception as e:
              print("Failed one dowload: " + e)

    with open("songData.txt", "w") as songDataFile:
        print("donesongs")
        songDataFile.write(json.dumps(songInfo))

    with open("idList.txt", "w") as idListFile:
        print("doneids")
        idListFile.write(json.dumps(idList))
