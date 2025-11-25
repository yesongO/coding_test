def solution(arr, intervals):
    result = []
    for a in intervals:
        for i in range(a[0], a[1]+1):
            result.append(arr[i])
    return result