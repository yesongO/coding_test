def solution(n, m, section): 
    is_painting = [True] * n
    result = 0
    for i in section:
        is_painting[i-1] = False
        
    for j in range(len(is_painting)): 
        if is_painting[j] == False:
            is_painting[j:j+m] = [True] * m
            result += 1
            
    return result