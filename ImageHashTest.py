from PIL import Image
import imagehash
#from download import downloadvid
#from scale import scaleclip
from video import Video

yt_opts = {'format': 'mp4'}
vidurl = 'https://www.youtube.com/watch?v=q6EoRBvdVPQ'
testvid = Video(vidurl, 'Yee-q6EoRBvdVPQ')
directory = 'testframes2'

testvid.download(yt_opts)
testvid.scale(180)
testvid.split(directory, 30)
