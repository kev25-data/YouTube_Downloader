from pytube import YouTube

yt = YouTube(input('Link: '))

yd = yt.streams.get_highest_resolution()
yd.download('/Users/kevinguillencisneros/Downloads/')
