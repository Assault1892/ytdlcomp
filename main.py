from yt_dlp import YoutubeDL

# URL
url = input(str("URL: "))
print("入力URL: " + url)
print(type(url))

# mode

while True:
    try:
        mode = int(input("\ntype | 1: mp4, 2: mp3, 3: wav, 4: cancel: "))
        break
e   except ValueError:
        pass

print("mode: " + str(mode))
print(type(mode))

if mode == 1: # mp4
    a
elif mode == 2: # mp3
    b
elif mode == 3: # wav
    e
else: # cancel
    d