def solution(keymap, targets):
    key_dict = {}
    for one_map in keymap: 
        for idx, val in enumerate(one_map):
            if val not in key_dict.keys():
                key_dict[val] = idx + 1
            else:
                key_dict[val] = min(key_dict[val], idx + 1)
                
    result = []         
    
    for target_string in targets: 
        cur_result = 0
        for alphabet in target_string: 
            if alphabet not in key_dict:
                result.append(-1)
                break
            cur_result += key_dict[alphabet]
        else: result.append(cur_result)  
        
    return result
            
