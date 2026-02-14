from collections import deque

def solution(k, m, score):
    answer_lst = []
    score_queue = deque(sorted(score, reverse=True))
    
    while len(score_queue) >= m:
        cur_lst = []
        for i in range(m): 
            cur_lst.append(score_queue.popleft())
        answer_lst.append(min(cur_lst) * m)
    
    return sum(answer_lst)
    
        
