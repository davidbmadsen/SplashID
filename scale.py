import moviepy.editor as mp

def scaleclip(height,filename):

    filename = filename + '.mp4'
    clip = mp.VideoFileClip(filename)
    clip_resized = clip.resize(height=height)
    clip_resized.write_videofile("test_resized.mp4")