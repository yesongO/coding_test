from collections import deque

def solution(s):
    my_queue = deque(s)
    result = 0
    
    while my_queue:
        first_str = my_queue[0]
        first_str_count = 1
        another_str_count = 0
        
        for i in range(1, len(my_queue)):
            if first_str == my_queue[i]:
                first_str_count += 1
            else:
                another_str_count += 1

            if first_str_count == another_str_count:
                for j in range(first_str_count * 2):
                    my_queue.popleft()
                result += 1
                break
        else:
            result += 1
            break
            
    return result
            
        
        
                                
        
        
    
            
        
        
        
        
    
    