def solution(arr):
    result = [arr[0]]
    for i in range(len(arr)-1): # 0, 1, 2, 3, 4, 5
        if arr[i] != arr[i+1]:
            result.append(arr[i+1])
    return result