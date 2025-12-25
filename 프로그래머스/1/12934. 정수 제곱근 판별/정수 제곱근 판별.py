def solution(n):
    if int(n ** 0.5) * int(n ** 0.5) == n:
        return ((n ** 0.5) + 1) ** 2
    else:
        return -1