'''
#source_frames = os.listdir('source')
#source_hashes = []

# Hash source frames


print("[Source frames] Hashing...")
for source_frame in source_frames:
    hash_from_source = imagehash.phash(Image.open('./source/' + source_frame))
    source_hashes.append(hash_from_source)
print("[Source frames] Done.")
'''

'''
print("[Video frames] Hashing...")
for frame in frames:
    hash_from_frame = imagehash.phash(Image.open('./' + directory + '/' + frame))
    frame_hashes.append(hash_from_frame)
print("[Video frames] Done.")


# Compare all source frames against all video frames
print("[Frame compare] Comparing frames...")
comparisons = []  # List of comparisons for one frame
for i in range(len(source_hashes)):
    for j in range(len(frame_hashes)):
        result = (source_hashes[i] - frame_hashes[j])
        comparisons.append(result)
    all_comparisons.append(comparisons)     # Add to list of comparison vectors
    comparisons = []                        # Clear comparisons for next comparison sequence
frame_hashes = []
print("[Frame compare] Done.")
'''