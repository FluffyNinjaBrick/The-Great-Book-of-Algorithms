

def counting_sort(array, max_elem):
    count_arr = [0 for x in range(max_elem + 1)]
    result_arr = [0 for x in range(len(array))]
    for number in array:
        count_arr[number] += 1
    for i in range(max_elem + 1):
        count_arr[i+1] += count_arr[i]
    for number in array:
        count_arr[number] -= 1
        result_arr[count_arr[number]] = number
    return result_arr
