from pytube import YouTube

yt = YouTube(input('Link: '))

yd = yt.streams.get_audio_only()
yd.download()