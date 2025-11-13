def solution(x):
    result = []
    result.append(x)
    while (x > 1):
        if x % 2 == 0:
            x = x // 2
            result.append(x)
        else:
            x = x * 3 + 1
            result.append(x)
    return result