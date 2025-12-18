def solution(a, b, n):
    empty_bottle = n
    get_bottle = 0
    
    while empty_bottle >= a:
        cur_get_bottle = 0
        get_bottle += (empty_bottle // a) * b  
        cur_get_bottle += (empty_bottle // a) * b
        empty_bottle = (empty_bottle - (empty_bottle // a) * a) + cur_get_bottle 
        
    return get_bottle
            
    
        