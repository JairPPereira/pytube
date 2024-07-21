from pytube import YouTube
YouTube('https://youtu.be/F1vezvMir4o?si=2n8rccO0q10QXRUX').streams.first().download()
yt = YouTube('https://youtu.be/F1vezvMir4o?si=2n8rccO0q10QXRUX')
stream = yt.streams.get_by_itag(22)
stream.download()