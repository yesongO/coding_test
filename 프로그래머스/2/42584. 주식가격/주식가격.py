from collections import deque

def solution(prices):
    queue = deque(prices)
    result = [0] * len(prices)
    
    if len(prices) == 1:
        return [0]
    
    for i in range(len(prices)-1):
        cur_time = 0
        cur_num = queue.popleft()
        for j in range(i+1, len(prices)):
            if cur_num <= prices[j]:
                cur_time += 1
            else:
                cur_time += 1
                break
        result[i] = cur_time
        
    return result