def solution(food):
    one_side = ""
    for i in range(1, len(food)):
        one_side += str(i) * (food[i] // 2)
    return one_side + "0" + one_side[::-1]
            
        
        