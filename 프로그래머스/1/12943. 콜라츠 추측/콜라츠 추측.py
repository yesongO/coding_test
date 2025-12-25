def solution(num):
    result = 0
    if num == 1:
        return 0
    while num != 1:
        if (num % 2 == 0) and (result < 500):
            num = num / 2
            result += 1
        elif (num % 2 != 0) and (result < 500):
            num = num * 3 + 1
            result += 1
        else:
            return -1
    return result
        