
# an algorithm for sorting an array of 0s and 1s. It's exactly as simple as you think it is


def sort_binary_array(array):
    ones = 0
    for i in range(len(array)):
        ones += array[i]
    for i in range(len(array) - ones):
        array[i] = 0
    for i in range(len(array) - ones, len(array)):
        array[i] = 1


if __name__ == "__main__":
    to_sort = [1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1]
    sort_binary_array(to_sort)
    print(to_sort)