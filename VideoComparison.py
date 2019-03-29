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
    print("[Hash frames] Hashing", directory[:-11], "with hash size", hash_size)
    start_time = time.time()

    # Hash frames in folder
    for frame in frames_list:
        hashed_image = imagehash.phash(Image.open('./' + directory + '/' + frame), hash_size)
        hash_list.append(hashed_image)
    stop_time = time.time() - start_time
    print("[Hash frames] Done.", "Elapsed time: ", round(stop_time, 3), "seconds")

    return hash_list


def compare_frames(source_hashes, frame_hashes, hash_size):

    comparisons, all_comparisons = [], []
    print("[Frame compare] Finding most similar frame...")
    start_time = time.time()
    for i in range(len(source_hashes)):
        for j in range(len(frame_hashes)):
            result = round((source_hashes[i] - frame_hashes[j])/(hash_size ** 2), 5)
            comparisons.append(result)
        all_comparisons.append(comparisons)

        comparisons = []

    # Pick most similar frame based on hamming distance
    most_similar_frame = min(all_comparisons)
    print("[Frame compare] Done. Elapsed time:", round(time.time() - start_time, 3))

    return most_similar_frame


def compare_videos(source_id, show_plot=False, hash_size=8):

    os.chdir(os.path.dirname(__file__) + '/video')

    # Get all folders containing frames to compare
    dirs = os.listdir('./comparison')
    # Hash source frames
    source_hashes = hash_frames('./assets/' + source_id, hash_size)

    # Loop compares image in first directory with image in source directory
    for directory in dirs:

        print("[Video compare] Processing directory", directory)

        # Hash video frames
        frame_hashes = hash_frames('./comparison/' + directory, hash_size)

        # Compare all source frames against all video frames
        most_similar_frame = compare_frames(source_hashes, frame_hashes, hash_size)

        # Filter out noise
        filtered_result = savgol_filter(most_similar_frame, 201, 6)

        avg_base = np.mean(most_similar_frame)
        avg_savgol_1 = np.mean(filtered_result)
        print("Mean (unfiltered):", avg_base)
        print("Mean             :", avg_savgol_1)

        if show_plot:
            fig = plt.figure()
            plt.plot(filtered_result)
            plt.title("Video: ")
            #plt.ylim(0.3, 0.55)
            fig.suptitle('Hash size = ' + str(hash_size), fontsize=16)

            plt.show()