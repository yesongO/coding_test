def solution(k, score):
    result = []
    acc = []
    for i in range(len(score)): 
        acc.append(score[i])
        if len(acc) < k:
            result.append(min(acc))
        else:
            result.append(sorted(acc, reverse=True)[k-1])
    return result
            
        
        
    