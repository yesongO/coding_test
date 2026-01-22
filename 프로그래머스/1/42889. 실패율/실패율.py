from collections import deque

def solution(N, stages):
    failure_rate_for_stage = [[0, i+1] for i in range(N)]  
    
    stage_queue = deque(sorted(stages)) 
    
    for i in range(N):
        cur_stage = i + 1
        store_user_len = len(stage_queue) 
        cur_stage_user_num = 0
        
        while stage_queue and cur_stage == stage_queue[0]:
            stage_queue.popleft()
            cur_stage_user_num += 1
        
        if store_user_len == 0:
            failure_rate = 0
        else:
            failure_rate = cur_stage_user_num / store_user_len
            
        failure_rate_for_stage[i][0] += failure_rate
        
    return [stage for _, stage in sorted(failure_rate_for_stage, key=lambda x: (-x[0],x[1]))]
                                         
                                



