from __future__ import unicode_literals
import youtube_dl
import os

def downloadvid(url):

    ydl_opts = {
        'format' : 'mp4'
    }

    os.chdir("video")
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])