# ========== UNTESTED ========== #
# an implementation of Kadane's algorithm.


def kadane(array):
    max_local = max_global = max_global_end_idx = max_global_len = curr_len = 0
    for i in range(len(array)):
        max_local = max_local + array[i]
        if max_local < 0:
            max_local = 0
            curr_len = 0
        else:
            curr_len += 1
        if max_local > max_global:
            max_global = max_local
            max_global_end_idx = i
            max_global_len = curr_len
    return [max_global_len, max_global_end_idx]