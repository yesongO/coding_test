def solution(my_string, indices):
    result = ''
    for i in range(len(my_string)): # 0 ~ 18
        if (i not in indices):
            result += my_string[i]
    return result
        
        