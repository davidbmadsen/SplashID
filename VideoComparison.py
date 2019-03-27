from PIL import Image
import imagehash
import os
import matplotlib.pyplot as plt
import numpy as np


def hash_frames(directory):
    hash_list = []
    frames_list = os.listdir(directory)
    frames_tmp = []
    # Get frames and sort them
    for frame in frames_list:
        frames_tmp.append(int(frame[:-4]))
    frames_tmp.sort()

    # Create new sorted frame list
    frames = []
    for frame in frames_tmp:
        frames.append(str(frame) + '.jpg')
    print("[Hash frames] Hashing...")

    for frame in frames_list:
        hashed_image = imagehash.phash(Image.open('./' + directory + '/' + frame))
        hash_list.append(hashed_image)
    print("[Hash frames] Done.")

    return hash_list


def compare_frames(source_hashes, frame_hashes):
    comparisons = []
    all_comparisons = []
    print("[Frame compare] Comparing frames...")
    for i in range(len(source_hashes)):
        for j in range(len(frame_hashes)):
            result = (source_hashes[i] - frame_hashes[j])
            comparisons.append(result)

        all_comparisons.append(comparisons)     # Add to list of comparison vectors
        comparisons = []                        # Clear comparisons for next comparison sequence
    print("[Frame compare] Done.")

    return all_comparisons


def compare_videos(show_plot=False, scaling_factor=(1/5)):

    os.chdir('video')

    # Get all folders containing frames to compare
    dirs = list(filter(lambda x: os.path.isdir(x) and str.startswith(x, 'frames'), os.listdir('.')))

    # Create source frames
    source_hashes = hash_frames('source')
    print(len(source_hashes))

    # Loop compares image in first directory with image in source directory
    for directory in dirs:
        print("[Video compare] Processing directory", directory)

        # Hash video frames
        frame_hashes = hash_frames(directory)

        # Compare all source frames against all video frames
        all_comparisons = compare_frames(source_hashes, frame_hashes)

        # Multiply together results - np.array() used to simplify element-wise multiplication
        comparisons = np.array(all_comparisons[0])

        for i in range(len(all_comparisons)):            # Goes through all comparison lists
            tmp = np.array(all_comparisons[i])
            comparisons = (comparisons * tmp) ** scaling_factor

        if show_plot:
            plt.plot(comparisons)
            plt.show()

compare_videos(True)
