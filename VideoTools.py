from __future__ import unicode_literals
import youtube_dl
import moviepy.editor as mp
import os
import cv2


def split_into_frames(url, height, frameskip, subfolder):

    # Change directory to ./video/
    os.chdir("video")

    # Download video
    opts = {'format': 'mp4',
            'outtmpl': '%(id)s.mp4'}

    with youtube_dl.YoutubeDL(opts) as ydl:
        info_dict = ydl.extract_info(url)
        video_id = info_dict.get("id", None) + '.mp4'

    clip = mp.VideoFileClip(video_id)
    clip_resized = clip.resize(height=height)
    clip_resized.write_videofile(video_id + '-resized.mp4')
    resized_name = video_id + '-resized.mp4'

    # Split into frames
    cap = cv2.VideoCapture(resized_name)

    try:
        if not os.path.exists(str(subfolder)):
            os.makedirs(str(subfolder))
    except OSError:
        print('Error: Creating directory of data')

    current_frame = 0
    while True:

        ret, frame = cap.read()
        if not ret:
            break

        name = './' + str(subfolder) + '/' + str(int(current_frame/frameskip))
        cv2.imwrite(name + '.jpg', frame)

        current_frame += frameskip
