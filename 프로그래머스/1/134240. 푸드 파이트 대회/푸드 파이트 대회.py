def solution(food):
    half_result = ''
    for i in range(1, len(food)):
        count = food[i] // 2
        for j in range(count):
            half_result += str(i)
        
    return half_result + '0' + half_result[::-1]
        
        
        