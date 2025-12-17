def solution(name, yearning, photo):
    yearning_dic = dict(zip(name, yearning))
    result = []
    for p in photo:
        score = 0
        for name in p:
            if name in yearning_dic:
                score += yearning_dic[name]
        result.append(score)
    return result
            
            
    