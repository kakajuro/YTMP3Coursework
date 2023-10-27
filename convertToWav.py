import os
#from pydub import AudioSegment
import subprocess
currentPath = "./songs"
newPath = f"{currentPath}/newSongs"

total = len(os.listdir(currentPath))
current = 1

for file in os.listdir(currentPath):
  
  if os.path.isfile(os.path.join(currentPath, file)):
    
    try:
     
      newFilename = file.replace(".mp3", ".wav")
      
      baseArray = ["ffmpeg", "-i"]
      
      baseArray.append(os.path.join(currentPath, file))
      baseArray.append(os.path.join(newPath, newFilename))
      
      subprocess.call(baseArray)
      
      #sound = AudioSegment.from_mp3(os.path.join(currentPath, file))
      #sound.export(newPath, format="wav")

      print(f"Conversion of {newFilename} completed. {current}/{total}")
      
    except:
      print(f"Failure! {current}/{total}")
    finally:
      current+=1