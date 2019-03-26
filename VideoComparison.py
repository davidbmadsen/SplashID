from PIL import Image
import imagehash
import os
import matplotlib.pyplot as plt
import numpy as np
import time

def compare_videos(show_plot=False):

    os.chdir('video')

    # Get all folders containing frames to compare
    dirs = list(filter(lambda x: os.path.isdir(x) and str.startswith(x, 'frames'), os.listdir('.')))

    comparisons = []        # List of comparisons for one frame
    all_comparisons = []    # List of all comparison arrays

    # Create source frames list
    source_frames = os.listdir('source')

    # Loop compares image in first directory with image in source directory
    for directory in dirs:

        frames = list(os.listdir(directory))
        frames_int = []                 # list of integers corresponding to frames that are to be compared

        # Get frames and sort them
        for frame in frames:
            frame_number = frame[:-4]   # remove file extension (.jpg)
            frames_int.append(int(frame_number))
        frames_int.sort()

        # Create new sorted frame list
        frames = []
        for frame in frames_int:
            frames.append(str(frame) + '.jpg')

        # Compare all frames to all source frames
        for source_frame in source_frames:
            start_time = time.time()
            print("Processing frame ", source_frame, " of ", str(len(source_frames)), "...")

            for frame in frames:
                #print("Comparing frame " + source_frame + " to " + frame)
                hash_from_frame = imagehash.phash(Image.open('./' + directory + '/' + frame), 8)
                hash_from_source = imagehash.phash(Image.open('./source/' + source_frame), 8)
                result = (hash_from_frame - hash_from_source)
                comparisons.append(result)
            all_comparisons.append(comparisons)     # Add to list of comparison vectors
            comparisons = []                        # Clear comparisons
            print("[%s Elapsed]" % (time.time() - start_time))

        # Multiply together results
        comparisons = np.array(all_comparisons[0])
        for i in range(len(all_comparisons)):            # Goes through all comparison lists
            tmp = np.array(all_comparisons[i])
            comparisons = (comparisons * tmp) ** (1/3)

        if show_plot:
            plt.plot(comparisons)
            plt.show()

compare_videos(True)
