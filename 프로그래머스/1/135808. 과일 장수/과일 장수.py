from collections import deque

def solution(k, m, score):
    apple_sorted_queue = deque(sorted(score, reverse=True))
    result = 0
    
    while len(apple_sorted_queue) >= m:
        for i in range(m):
            apple_arr = []
            apple_arr.append(apple_sorted_queue.popleft())
        min_val = min(apple_arr)
        result += min_val * m
            
    return result
