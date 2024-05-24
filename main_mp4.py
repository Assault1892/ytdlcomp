from yt_dlp import YoutubeDL
import os

filepath = os.getcwd()

# === URL
url = input(str("URL: "))
print("入力URL: " + url)
# print(type(url))

dl_option = {
    "restrictfilenames": "true", # ファイル名をASCII文字列に制限
    "format": "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]", # 最高品質mp4
    "outtmpl": f"{filepath}/outputs/mp4/%(title)s.%(ext)s" 
}

with YoutubeDL(dl_option) as ydl:
    res = ydl.download(url)