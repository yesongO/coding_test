def solution(my_string, queries):
    my_str = list(my_string)
    for lst in queries:
        oppose = []
        s, e = lst[0], lst[1]
        for i in range(e, s-1, -1):
            oppose.append(my_str[i])
        my_str[s:e+1] = oppose[:]
        
    return "".join(my_str)