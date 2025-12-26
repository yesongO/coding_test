def solution(n):
    result = []
    for i in str(n):
        result.append(i)
    result.sort(reverse = True)
    return int(''.join(result))