def solution(n, k):
    i = 1
    result = []
    while (i <= n):
        if i % k == 0:
            result.append(i)
        i += 1
    return result