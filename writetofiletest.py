import imagehash
import time
from PIL import Image
'''
start_time = time.time()
hash1 = imagehash.phash(Image.open('65.jpg'), 64)
print("Elapsed time small: ", time.time() - start_time)
'''
start_time2 = time.time()
hash2 = imagehash.phash(Image.open('65.jpg'), 64)
print("Elapsed time large: ", time.time() - start_time2)
