def solution(k, score):
    lowest_honer_score = [] 
    cur_score_lst = [] 
    
    for i in range(len(score)):
        cur_score_lst.append(score[i])
        if i < k:
            lowest_honer_score.append(min(cur_score_lst))
        else:
            lowest_honer_score.append(sorted(cur_score_lst, reverse=True)[k-1])
            
    return lowest_honer_score