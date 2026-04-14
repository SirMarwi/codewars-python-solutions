def solution(number):
    running_sum = 0
    
    if number < 0:
        return 0
    
    for i in range(1, number):
        if i % 3 == 0:
            running_sum += i
        elif i % 5 == 0:
            running_sum += i
    return running_sum
  
