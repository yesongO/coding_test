from collections import deque

def solution(n, m, section):
    init_lst = [1] * n
    for i in section:
        init_lst[i-1] = 0
    
    drawing_queue = deque(init_lst)
    result = 0
    
    while drawing_queue:
        if drawing_queue[0] == 1:
            drawing_queue.popleft()
        else:
            result += 1
            for _ in range(m):
                if drawing_queue: drawing_queue.popleft()
                else: break
            
    return result


