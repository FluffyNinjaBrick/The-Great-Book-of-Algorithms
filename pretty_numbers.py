
# In a number we can specify single digits - those that show up once, and multiple digits - those
# that show up many times. A number is prettier than another if it has more single digits than the other,
# or if those numbers are tied, if it has fewer multiple digits. Implement pretty_sort, a function that sorts
# the numbers from prettiest to ugliest.


# check prettiness of number
def check_pretty(num):
    counter = [0 for i in range(10)]
    while num:
        counter[num % 10] += 1
        num /= 10
    single = 0
    multi = 0
    for i in range(10):
        if counter[i] == 1:
            single += 1
        elif counter[i] > 1:
            multi += 1
    return single, multi


# sort them, radix-like
def special_counting_sort(num_arr, prettiness_arr, mode):
    result = [0 for i in range(len(num_arr))]
    # sort by single
    if mode == "single":
        max_single = 0
        for single, _ in range(len(prettiness_arr)):
            if single > max_single:
                max_single = single
        count_arr = [0 for i in range(max_single)]
        for i in range(len(num_arr)):
            count_arr[prettiness_arr[i][0]] += 1
        for i in range(len(count_arr) - 1):
            count_arr[i+1] += count_arr[i]
        for i in range(len(num_arr)):
            count_arr[prettiness_arr[i][0]] -= 1
            result[count_arr[prettiness_arr[i][0]]] = num_arr[i]
    # sort by multiple
    elif mode == "multi":
        max_multi = 0
        for _, multi in range(len(prettiness_arr)):
            if multi > max_multi:
                max_multi = multi
        count_arr = [0 for i in range(max_multi)]
        for i in range(len(num_arr)):
            count_arr[prettiness_arr[i][1]] += 1
        for i in range(len(count_arr) - 1):
            count_arr[i+1] += count_arr[i]
        for i in range(len(num_arr)):
            count_arr[prettiness_arr[i][1]] -= 1
            result[count_arr[prettiness_arr[i][1]]] = num_arr[i]
    return result


def pretty_sort(nums):
    prettiness = []
    for i in range(len(nums)):
        prettiness[i] = check_pretty(nums[i])
    sorted_by_multi = special_counting_sort(nums, prettiness, "multi")
    fully_sorted = special_counting_sort(sorted_by_multi, prettiness, "single")
    return fully_sorted


if __name__ == "__main__":