def solution(a, b, c, d):
    list_ = [a, b, c, d]
    set_ = {a, b, c, d}
    min_val, max_val = min(a, b, c, d), max(a, b, c, d)
    score = 0
    
    if len(set_) == 1: # 1번경우
        score = 1111 * a
    elif len(set_) == 2:
        if list_.count(list_[0]) == 2: # 3번경우
            score = (min_val + max_val) * (max_val - min_val)
        else: # 2번경우
            p, q = 0, 0
            for i in list_:
                if list_.count(i) == 3:
                    p = i
                if list_.count(i) == 1:
                    q = i
            score = (10 * p + q) ** 2
    elif len(set_) == 3: #4번경우
        for i in list_:
            if list_.count(i) == 2:
                list_.remove(i)
                list_.remove(i)
        score = list_[0] * list_[1]
    elif len(set_) == 4: # 5번경우
        score = min_val
    return score