from PIL import Image
import imagehash
import os
import matplotlib.pyplot as plt
import time
import numpy as np
from scipy.signal import savgol_filter

def hash_frames(directory, hash_size=8):
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
    print("[Hash frames] Hashing", directory, "with hash size", hash_size)
    start_time = time.time()

    # Hash frames in folder
    for frame in frames_list:
        hashed_image = imagehash.phash(Image.open('./' + directory + '/' + frame), hash_size)
        hash_list.append(hashed_image)
    stop_time = time.time() - start_time
    print("[Hash frames] Done.", "Elapsed time: ", round(stop_time, 3), "seconds")

    return hash_list


def compare_frames(source_hashes, frame_hashes, hash_size):

    comparisons = []
    all_comparisons = []
    print("[Frame compare] Finding most similar frame...")
    for i in range(len(source_hashes)):
        for j in range(len(frame_hashes)):
            result = round((source_hashes[i] - frame_hashes[j])/(hash_size ** 2), 5)
            comparisons.append(result)
        all_comparisons.append(comparisons)
        comparisons = []

    # Pick most similar frame based on hamming distance
    most_similar_frame = min(all_comparisons)
    print("[Frame compare] Done.")

    return most_similar_frame


def compare_videos(show_plot=False, hash_size=8, scaling_factor=(1/4)):

    os.chdir('video')

    # Get all folders containing frames to compare
    dirs = list(filter(lambda x: os.path.isdir(x) and str.startswith(x, 'frames'), os.listdir('.')))

    # Create source frames
    source_hashes = hash_frames('source', hash_size)

    # Loop compares image in first directory with image in source directory
    for directory in dirs:
        print("[Video compare] Processing directory", directory)

        # Hash video frames
        frame_hashes = hash_frames(directory, hash_size)

        # Compare all source frames against all video frames
        most_similar_frame = compare_frames(source_hashes, frame_hashes, hash_size)
        filtered_result = savgol_filter(most_similar_frame, 501, 6)
        filtered_result_2 = savgol_filter(most_similar_frame, 15, 3)
        avg_base = np.mean(most_similar_frame)
        avg_savgol_1 = np.mean(filtered_result)
        avg_savgol_2 = np.mean(filtered_result_2)
        if show_plot:
            plt.plot(most_similar_frame)
            plt.plot(filtered_result)
            plt.plot(filtered_result_2)
            plt.plot(avg_base)
            plt.plot(avg_savgol_1)
            plt.plot(avg_savgol_2)
            plt.show()

compare_videos(True, 64)
