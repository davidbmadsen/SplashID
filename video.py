from __future__ import unicode_literals
import youtube_dl
import moviepy.editor as mp
import os
import cv2

class Video:
    def __init__(self, url, filename):
        self.url = url
        self.filename = filename

    def download(self, opts={}):

        os.chdir("video")
        with youtube_dl.YoutubeDL(opts) as ydl:
            ydl.download([self.url])

    def scale(self, height):
        if self.filename[-4:] != '.mp4' and self.filename[-3:] != '.':
            self.filename += '.mp4'

        clip = mp.VideoFileClip(self.filename)
        clip_resized = clip.resize(height=height)
        clip_resized.write_videofile("test_resized.mp4")

    def split(self, subfolder, frameskip, filetype = '.jpg'):

        video = cv2.VideoCapture(self.filename)

        try:
            if not os.path.exists(str(subfolder)):
                os.makedirs(str(subfolder))
        except OSError:
            print('Error: Creating directory of data')

        current_frame = 0
        while (True):

            ret, frame = video.read()
            if ret == False:
                break

            name = './' + str(subfolder) + '/' + str(int(current_frame/frameskip)) + filetype
            cv2.imwrite(name, frame)

            current_frame += frameskip
