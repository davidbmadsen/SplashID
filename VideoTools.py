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


def split_into_frames(url, is_source=False):

    # Change directory to ./video/
    os.chdir(os.path.dirname(__file__) + '/video')

    # Download videos
    opts = {'format': '18',
            'outtmpl': '%(id)s.mp4',
            'extractaudio': False}

    with youtube_dl.YoutubeDL(opts) as ydl:
        info_dict = []
        video_id = []
        for index, url in enumerate(url):
            info_dict.append(ydl.extract_info(url))
            video_id.append(info_dict[index].get("id", None) + '.mp4')


    for index, vid in enumerate(video_id):

        print("Splitting " + str(vid) + " into frames...")

        # Capture video
        cap = cv2.VideoCapture(vid)
        if is_source:
            framedir = './assets/' + vid[0:11]
        else:
            framedir = './comparison/' + vid[0:11]

        try:
            if not os.path.exists(framedir):
                os.makedirs(framedir)
        except OSError:
            print('Error: Creating directory of data')

        if len(os.listdir(framedir)) != 0:
            print("Frames already created.")
            break

        # Split capture into frames
        current_frame = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Framesplit done.")
                break
            height = frame.shape[0]
            width = frame.shape[1]
            x = int((width - height) / 2)

            name = './' + framedir + '/' + str(int(current_frame))
            cv2.imwrite(name + '.jpg', frame[0:height, x:x + height])

            current_frame += 1
