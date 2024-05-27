from yt_dlp import YoutubeDL
import os
import sys

filepath = os.getcwd()
mode = 0

def download(url, dltype):
    if dltype == 1: # mp4
        dl_option = {
        "restrictfilenames": "true", # ファイル名をASCII文字列に制限
        "format": "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]", # 最高品質mp4
        "outtmpl": f"{filepath}/outputs/mp4/%(title)s.%(ext)s" 
    }
    elif dltype == 2: # mp3
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
    elif dltype == 3: # wav
        dl_option = {
        "restrictfilenames": "true", # ファイル名をASCII文字列に制限
        "format": "wav/bestaudio/best",
        "outtmpl": f"{filepath}/outputs/wav/%(title)s.%(ext)s" 
    }
    else:
        print("bye!\n")
        sys.exit()
    
    with YoutubeDL(dl_option) as ydl:
        res = ydl.download(url)
    print("download completed; return back to url...\n")

while True:
    url = input(str("URL: "))
    while True:
        try:
            dltype = int(input("1: best mp4, 2: mp3, 3: bestaudio (wav), 4: cancel: "))
            break
        except ValueError:
            pass
    if dltype > 4:
        print("bye!\n")
        sys.exit()
    else:
        download(url, dltype)