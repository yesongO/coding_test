def solution(name, yearning, photo):
    yearning_dict = dict(zip(name, yearning))
    result = [0] * len(photo)
    
    for idx, lst in enumerate(photo):
        for name in lst:
            result[idx] += yearning_dict.get(name, 0)
            
    return result
            
            
    