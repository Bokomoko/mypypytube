from pytube import YouTube
which_video_url = "https://youtu.be/J5TE5jhNgE8"
YouTube(which_video_url).streams.first().download()
yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')

print(yt.streams)


# .filter(progressive=True, file_extension='mp4')
# .order_by('resolution')
# .desc()
# .first()
# ..download()
