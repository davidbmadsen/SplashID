def find_most_similar(list source_hashes,list frame_hashes, int hash_size):
    cdef int i
    cdef int j
    cdef list comparisons = []
    cdef list all_comparisons = []

    for i in range(len(source_hashes)):
        for j in range(len(frame_hashes)):
            result = round((source_hashes[i] - frame_hashes[j])/(hash_size ** 2), 5)
            comparisons.append(result)
        all_comparisons.append(comparisons)

        comparisons = []

    most_similar_frame = min(all_comparisons)
    return most_similar_frame


