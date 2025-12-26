def solution(n):
    str_n = str(n)
    result = []
    for i in range(-1, -len(str_n)-1, -1):
        result.append(int(str_n[i]))
    return result
        