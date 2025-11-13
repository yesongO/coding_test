def solution(l, r):
    answer = []
    for i in range(l, r+1): # 5, 6, 7, .... 50 .. 55 .. 500 ... 
        cur_num = str(i) # "505"
        if set(cur_num) <= {"0", "5"}:
            answer.append(int(cur_num))
    if len(answer) == 0:
        answer.append(-1)

    return answer