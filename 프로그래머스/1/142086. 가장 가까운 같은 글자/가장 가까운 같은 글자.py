def solution(s):
    result = []
    for idx, str in enumerate(s):
        cur_front = 0
        for i in range(idx-1, -1, -1):
            if s[i] == str:
                cur_front += 1
                result.append(cur_front)
                break
            else:
                cur_front += 1
        else:
            result.append(-1)
    return result
        