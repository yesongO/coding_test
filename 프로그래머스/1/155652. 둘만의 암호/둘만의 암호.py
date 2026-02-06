def solution(s, skip, index):
    alphabet_str = 'abcdefghijklmnopqrstuvwxyz';
    alphabet_lst = list(alphabet_str)
    for i in skip:
        alphabet_lst.remove(i)
        
    cur_alphabet_length = len(alphabet_lst) 
    
    result = ''
    
    for alphabet in s:
        cur_idx = alphabet_lst.index(alphabet) + index
        if cur_idx < cur_alphabet_length:
            result += alphabet_lst[cur_idx]
        else:
            cur_idx = cur_idx % cur_alphabet_length
            result += alphabet_lst[cur_idx]
    return result

