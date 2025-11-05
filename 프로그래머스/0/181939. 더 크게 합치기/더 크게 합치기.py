def solution(a, b):
    answer = 0
    case_one = int(str(a) + str(b))
    case_two = int(str(b) + str(a))
    
    if case_one >= case_two:
        answer += case_one
    else:
        answer += case_two
    return answer