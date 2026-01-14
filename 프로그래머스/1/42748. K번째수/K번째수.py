def solution(array, commands):
    result = []
    for i, j, k in commands:
        sorted_arr = sorted(array[i-1:j])
        result.append(sorted_arr[k-1])
    return result