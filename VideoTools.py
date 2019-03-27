from __future__ import unicode_literals
from bs4 import BeautifulSoup as bs
import os, cv2, youtube_dl, requests
import moviepy.editor as mp


def get_search(qstring, results):

    base = "https://www.youtube.com/results?search_query="
    r = requests.get(base + qstring)

    page = r.text
    soup = bs(page, 'html.parser')

    vids = soup.findAll('a', attrs={'class': 'yt-uix-tile-link'})

    videolist = []
    for v in vids:
        tmp = 'https://www.youtube.com' + v['href']
        videolist.append(tmp)
    return videolist[0:results]


def split_into_frames(url, height, frameskip):

    # Change directory to ./video/
    os.chdir("video")

    # Download videos
    opts = {'format': 'mp4',
            'outtmpl': '%(id)s.mp4',
            'extractaudio': False}

    with youtube_dl.YoutubeDL(opts) as ydl:
        info_dict = []
        video_id = []
        resized_name = []
        for index, url in enumerate(url):
            info_dict.append(ydl.extract_info(url))
            print(info_dict[index])
            video_id.append(info_dict[index].get("id", None) + '.mp4')

    for index, vid in enumerate(video_id):
        # Resize clip
        clip = mp.VideoFileClip(video_id[index])
        clip_resized = clip.resize(height=height)
        clip_resized.write_videofile(video_id[index][0:11] + '-resized.mp4')

        resized_name = video_id[index][0:11] + '-resized.mp4'

        print("Splitting " + str(resized_name) + " into frames...")

        # Capture video
        cap = cv2.VideoCapture(resized_name)
        framedir = "frames_" + str(index)

        try:
            if not os.path.exists(framedir):
                os.makedirs(framedir)
        except OSError:
            print('Error: Creating directory of data')

        # Split capture into frames
        current_frame = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            name = './' + framedir + '/' + str(int(current_frame/frameskip))
            cv2.imwrite(name + '.jpg', frame)

            current_frame += frameskip
