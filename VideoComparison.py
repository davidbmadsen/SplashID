from PIL import Image
import imagehash
import os
import matplotlib.pyplot as plt
import numpy as np
def CompareVideos(framepath):

    os.chdir('video')

    # Get all folders containing frames to compare
    dirs = list(filter(lambda x: os.path.isdir(x) and str.startswith(x, 'frames'), os.listdir('.')))

    comparisons = []
    # Loop compares image in first directory with image in source directory
    for directory in dirs:

        frames = list(os.listdir(directory))
        frames_int = []
        for frame in frames:
            frame_number = frame[:-4]
            frames_int.append(int(frame_number))
        frames_int.sort()

        frames = []
        for frame in frames_int:
            frames.append(str(frame) + '.jpg')
        print(frames)
        for frame in frames:
            hash_from_frame = imagehash.phash(Image.open('./' + directory + '/' + frame))
            hash_from_source = imagehash.phash(Image.open('./source/427.jpg'))
            result = hash_from_frame - hash_from_source
            comparisons.append(result**(1/3))

    y_axis = np.linspace(0, 10, 100)
    #fig = plt.figure()
    plt.plot(comparisons)
    plt.show()
    print(comparisons)
    '''
    for frame in frames:
        hash = imagehash.phash(frame)
        hashes.append(hash)
    # Take in frames

    # Run pHash

    # Store in array
    '''

CompareVideos('frames_0')