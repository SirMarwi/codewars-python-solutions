def find_outlier(integers):
    odd = []
    even = []
    for number in integers:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
        
    return odd[0] if len(odd) == 1 else even[0]
    