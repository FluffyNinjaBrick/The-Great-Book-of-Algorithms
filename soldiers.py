# TASK - we have a bunch of soldiers' heights in an unsorted array. Supposing we arranged them in a line
#        ordering by ascending height, find the heights of the soldiers on positions between p and q.


# find shortest and tallest soldier. Counting sort needs this. Linear complexity.
def find_min_max(arr):
    minimum = 1000000
    maximum = 0
    for i in range(len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]
        if arr[i] > maximum:
            maximum = arr[i]
    return minimum, maximum


# Counting sort. We decrement the heights of the soldiers by the height of the shortest one, that way
# the count_arr becomes shorter. Linear complexity.
def counting_sort(arr, shortest, tallest):
    output_arr = [0 for i in range(len(arr))]
    heights = tallest - shortest + 1
    count_arr = [0 for i in range(heights)]
    for i in range(len(arr)):
        count_arr[arr[i] - shortest] += 1
    for i in range(len(count_arr) - 1):
        count_arr[i+1] += count_arr[i]
    for i in range(len(arr)):
        count_arr[arr[i] - shortest] -= 1
        output_arr[count_arr[arr[i] - shortest]] = arr[i]
    return output_arr


# the actual function
def section(soldiers, p, q):
    shortest, tallest = find_min_max(soldiers)
    sorted_soldiers = counting_sort(soldiers, shortest, tallest)
    result = []
    for idx in range(p, q + 1):
        result.append(sorted_soldiers[idx])
    return result


if __name__ == "__main__":
    from_idx = 4
    to_idx = 6
    test_soldiers = [10, 45, 70, 18, 13, 55, 23, 48]
    print(section(test_soldiers, from_idx, to_idx))
