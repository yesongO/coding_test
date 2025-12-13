def solution(s):
    result = []
    for i in range(len(s)): 
        cur_s = s[i]
        for j in range(i-1,-1,-1):
            if s[j] == cur_s:
                result.append(i-j)
                break    
        else: result.append(-1)
    return result