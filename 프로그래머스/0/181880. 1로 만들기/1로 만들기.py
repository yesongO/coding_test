def solution(num_list):
    result = []
    for i in num_list:
        add = 0
        while (i != 1):
            if (i % 2 == 0):
                i = i // 2
                add += 1
            elif (i % 2 != 0):
                i = (i - 1) // 2
                add += 1
        result.append(add)
    return sum(result)