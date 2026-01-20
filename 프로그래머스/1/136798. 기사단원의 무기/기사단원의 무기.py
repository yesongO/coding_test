from collections import deque

def solution(number, limit, power):
    divisor_count_lst = [0] * (number+1)
    
    for i in range(1, number+1):
        for j in range(i, number+1, i):
            divisor_count_lst[j] += 1
    
    divisor_count_deque = deque(divisor_count_lst)
    result = 0
    while divisor_count_deque:
        a = divisor_count_deque.popleft()
        if a <= limit:
            result += a
        else:
            result += power
    
    return result
        
