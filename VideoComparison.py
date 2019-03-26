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


    all_comparisons = []    # List of all comparison arrays
    firstframe = True
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

        comparisons = []  # List of comparisons for one frame

        # Compare all frames to all source frames -- This is what takes ages
        source_hashes, frame_hashes = [], []
        # Hash source frames
        print("[Source frames] Hashing...")
        for source_frame in source_frames:
            hash_from_source = imagehash.phash(Image.open('./source/' + source_frame))
            source_hashes.append(hash_from_source)
        print("[Source frames] Done.")

        # Hash video frames
        print("[Video frames] Hashing...")
        for frame in frames:
            hash_from_frame = imagehash.phash(Image.open('./' + directory + '/' + frame))
            frame_hashes.append(hash_from_frame)
        print("[Video frames] Done.")

        # Compare all source frames against all video frames
        for i in range(len(source_hashes)):
            start_time = time.time()
            for j in range(len(frame_hashes)):
                result = (source_hashes[i] - frame_hashes[j])
                comparisons.append(result)

            all_comparisons.append(comparisons)     # Add to list of comparison vectors
            comparisons = []                        # Clear comparisons
            print("Compared ", str(len(frame_hashes)), " frames in %s seconds" % round((time.time() - start_time), 3))

            if firstframe:
                print("Estimated time to complete: ", (len(frames)*len(source_frames))/round((time.time() - start_time), 3) % 60, " minutes")
                firstframe = False

        # Multiply together results
        comparisons = np.array(all_comparisons[0])
        for i in range(len(all_comparisons)):            # Goes through all comparison lists
            tmp = np.array(all_comparisons[i])
            comparisons = (comparisons * tmp) ** (1/3)

        if show_plot:
            plt.plot(comparisons)
            plt.show()

compare_videos(True)
