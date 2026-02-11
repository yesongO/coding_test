from collections import deque

def solution(number, limit, power):
    divisor_lst = [0] * (number + 1)
    
    for i in range(1, number+1):
        for j in range(i, number+1, i):
            divisor_lst[j] += 1
                    
    my_queue = deque(divisor_lst)
    result = 0
    
    while my_queue:
        cur_divisor = my_queue.popleft()
        if cur_divisor > limit:
            result += power
        else:
            result += cur_divisor
    
    return result
            
        
