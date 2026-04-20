def max_sequence(arr):
    max_sum = 0

    for i in range( len(arr)):
        curr_sum = 0
        for y in range(i,  len(arr)):
            curr_sum += arr[y]
            if curr_sum > max_sum:
                max_sum = curr_sum
    return max_sum

print(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]))
