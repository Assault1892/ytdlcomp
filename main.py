from yt_dlp import YoutubeDL
import os

filepath = os.getcwd()

# === URL
url = input(str("URL: "))
print("入力URL: " + url)
# print(type(url))

# === mode

while True:
    try:
        mode = int(input("1: best mp4, 2: mp3, 3: bestaudio (wav), 4: cancel: "))
        break
    except ValueError:
        pass

# print("mode: " + str(mode))
# print(type(mode))

if mode == 1: # mp4
    dl_option = {
        "restrictfilenames": "true", # ファイル名をASCII文字列に制限
        "format": "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]", # 最高品質mp4
        "outtmpl": f"{filepath}/outputs/mp4/%(title)s.%(ext)s" 
    }
    
    with YoutubeDL(dl_option) as ydl:
        res = ydl.download(url)

elif mode == 2: # mp3
    dl_option = {
        "restrictfilenames": "true", # ファイル名をASCII文字列に制限
        "format": "mp3/bestaudio/best",
        "outtmpl": f"{filepath}/outputs/mp3/%(title)s.%(ext)s",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3"
            }
        ]
    }
    
    with YoutubeDL(dl_option) as ydl:
        res = ydl.download(url)

elif mode == 3: # wav
    dl_option = {
        "restrictfilenames": "true", # ファイル名をASCII文字列に制限
        "format": "wav/bestaudio/best",
        "outtmpl": f"{filepath}/outputs/wav/%(title)s.%(ext)s" 
    }
    
    with YoutubeDL(dl_option) as ydl:
        res = ydl.download(url)
else: # cancel
    print("nope")