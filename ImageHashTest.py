from VideoTools import split_into_frames, get_search
from VideoComparison import *
yt_opts = {'format': 'mp4', 'outtmpl': '%(id)s'}
#vidurl = 'https://www.youtube.com/watch?v=q6EoRBvdVPQ'
#height = 180
filename = 'testvid'

# testvid.download(yt_opts)
# testvid.scale(180)
# testvid.split(directory, 30)


if __name__ == "__main__":

    #vidurl = get_search('yee', 2)
    source = ['https://www.youtube.com/watch?v=3_KUMt3DaDc']
    comparison = ['https://www.youtube.com/watch?v=8zXfycWyoU0']
    # compilation = ['https://youtu.be/8zXfycWyoU0']
    split_into_frames(source, True)
    split_into_frames(comparison)
    compare_videos('3_KUMt3DaDc', True, 32)
