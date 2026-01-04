def solution(numbers):
    result = set()
    for i in range(0, len(numbers)-1): # 0, 1, 2, 3
        for j in range(len(numbers)-(i+1)): # 0(0, 1, 2, 3) / 1(0, 1, 2)
            result.add(numbers[i] + numbers[i+j+1])
    return sorted(result)
        