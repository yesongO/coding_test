def solution(t, p):
    len_p = len(p)
    split_num_lst = []
    result = 0
    
    for i in range(len(t) - len_p + 1):
        split_num_lst.append(int(t[i:i+len_p]))
    
    for num in split_num_lst:
        if num <= int(p): result += 1
    
    return result