from PIL import Image
import imagehash
#from download import downloadvid
#from scale import scaleclip
from VideoTools import split_into_frames, get_search

yt_opts = {'format': 'mp4', 'outtmpl': '%(id)s'}
#vidurl = 'https://www.youtube.com/watch?v=q6EoRBvdVPQ'
height = 180
filename = 'testvid'

# testvid.download(yt_opts)
# testvid.scale(180)
# testvid.split(directory, 30)


if __name__ == "__main__":

    #vidurl = get_search('yee', 2)
    vidurl = ['https://www.youtube.com/watch?v=at4VxMl53vQ','https://www.youtube.com/watch?v=q6EoRBvdVPQ']
    split_into_frames(vidurl, height, 20)
