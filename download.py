import MostSimilarFrame
import timeit
import time
import os
from VideoComparison import *

directory = './video/comparison/8zXfycWyoU0'
source = './video/assets/q6EoRBvdVPQ'
source_hashes = hash_frames(source)
frame_hashes = hash_frames(directory)
start_time = time.time()
most_similar = MostSimilarFrame.find_most_similar(source_hashes, frame_hashes, 8)
print("Elapsed time:", time.time() - start_time)
