def solution(a, b):
    answer = 0
    
    plus = int(str(a) + str(b))
    multiply = 2 * a * b
    
    if plus >= multiply:
        answer += plus
    else:
        answer += multiply
        
    return answer