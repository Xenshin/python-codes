def max_in_array(arr):
    max = arr[0]
    for i in range(len(arr)):
        if (arr[i] > max):
            max = arr[i]
    return max

new_array = [12,56,74,2,54,18]
print(max_in_array(new_array))