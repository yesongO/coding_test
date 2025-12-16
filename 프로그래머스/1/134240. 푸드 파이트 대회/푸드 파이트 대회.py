def solution(food):
    one_side = ""
    for i in range(1, len(food)):
        if food[i] >= 2 and food[i] % 2 != 0:
            add_side_num = (food[i] - 1) // 2
            one_side += str(i) * add_side_num
        elif food[i] >= 2 and food[i] % 2 == 0:
            add_side_num = food[i] // 2
            one_side += str(i) * add_side_num
    return one_side + "0" + one_side[::-1]
            
        
        