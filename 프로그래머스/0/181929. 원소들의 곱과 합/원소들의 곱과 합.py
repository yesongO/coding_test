def solution(num_list):
    multi = 1
    sum = 0
    
    for i in num_list:
        multi *= i
        sum += i
        
    if multi < sum**2:
        return 1
    else:
        return 0