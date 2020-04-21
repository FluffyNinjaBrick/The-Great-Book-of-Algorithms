
# ============ UNTESTED ============ #
# Find longest bitonic sub-array of a given array. A bitonic array is one whose values rise, and then fall.


def find_bitonic(array):
    # at each index of asc we store the longest ascending array up to that idx,
    # at each index of desc the longest descending from that idx
    asc = [0 for i in range(len(array))]
    curr_len = 0
    for i in range(1, len(array)):
        if array[i-1] < array[i]:
            curr_len += 1
        else:
            curr_len = 0
        asc[i] = curr_len

    desc = [0 for i in range(len(array))]
    for i in range(len(array) - 2, -1, -1):
        if array[i+1] < array[i]:
            curr_len += 1
        else:
            curr_len = 0
        desc[i] = curr_len

    max_bitonic = 0
    middles = []
    # collect results - into an array, since there might be multiple bitonic arrays of equal length
    for i in range(len(array)):
        if asc[i] + desc[i] + 1 > max_bitonic:
            middles = [i]
        elif asc[i] + desc[i] + 1 == max_bitonic:
            middles.append(i)

    return middles
