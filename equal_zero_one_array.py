
# Within an array containing 1s and 0s, find longest possible sub-arrays which have an equal amount of 1s and 0s

# The idea is as follows. If we change all the 0s to -1s, a sub-array with an equal amount of both
# will add up to zero. We traverse the array, recording each sum we encounter. If we encounter a sum again,
# that means there is an array with the same amount of 0s and 1s between the current index and the index
# where we first encountered that sum


def find_subarrays(array):
    for i in range(len(array)):
        if array[i] == 0:
            array[i] = -1
    dict_sums = dict()
    curr_sum = 0
    max_len = 0

    for i in range(len(array) + 1):
        if curr_sum not in dict_sums.keys():
            dict_sums[curr_sum] = (i, 0)    # the tuple contains the start index and the length of the sub-array,
                                            # this is also what the return value consists of
        else:
            start, _ = dict_sums[curr_sum]
            curr_len = i - start
            dict_sums[curr_sum] = (start, curr_len)
            if curr_len > max_len:
                max_len = curr_len
        if i != len(array):
            curr_sum += array[i]

    longest_sublists = []
    for key in dict_sums.keys():
        curr_list = dict_sums[key]
        if curr_list[1] == max_len:
            longest_sublists.append(curr_list)
    return longest_sublists


if __name__ == "__main__":
    bin_array = [0, 0, 1, 0, 1, 0, 0]
    sublists = find_subarrays(bin_array)
    print(sublists)
