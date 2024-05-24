from yt_dlp import YoutubeDL
import os

filepath = os.getcwd()

# === URL
url = input(str("URL: "))
print("入力URL: " + url)
# print(type(url))

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