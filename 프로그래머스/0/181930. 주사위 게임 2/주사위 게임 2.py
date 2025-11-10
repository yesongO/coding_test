def solution(a, b, c):
    answer = 0
    my_set = {a, b, c}
    
    if len(my_set) == 3: 
        answer = a + b + c
    elif len(my_set) == 1: 
        answer = (3*a)*(3*a**2)*(3*a**3)
    else: 
        answer = (a+b+c)*(a**2+b**2+c**2)
    
    return answer