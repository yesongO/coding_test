def solution(keymap, targets):
    key_dict = {}
    for key in keymap:
        for idx, str in enumerate(key):
            if str not in key_dict:
                key_dict[str] = idx+1
            else:
                cur_val = key_dict[str]
                key_dict[str] = min(idx+1, cur_val)
                
    result = []
    for target in targets:
        target_sum = 0
        for s in target:
            if s not in key_dict: 
                result.append(-1) 
                break
            target_sum += key_dict[s]
        else:
            result.append(target_sum)
            
    return result
            
