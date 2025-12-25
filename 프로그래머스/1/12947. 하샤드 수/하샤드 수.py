def solution(x): 
    len_str_x = len(str(x)) 
    sum_str_x = 0
    for i in range(len_str_x):
        sum_str_x += int(str(x)[i])
    if x % sum_str_x == 0:
        return True
    else:
        return False 