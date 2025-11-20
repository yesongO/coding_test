def solution(my_string, m, c):
    lst = [] 
    answer = ''
    i = 0
    while len(lst) < int(len(my_string)) // m:
        lst.append(my_string[i:i+m])
        i = i + m
    for s in lst:
        answer = answer + s[c-1]
    return answer