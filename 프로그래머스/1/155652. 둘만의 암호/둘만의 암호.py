def solution(s, skip, index):
    all_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for a in skip:
        all_alphabet = all_alphabet.replace(a, "")
        
    result = ''
    for alphabet in s:
        cur_idx = all_alphabet.index(alphabet)
        new_idx = cur_idx + index
        if new_idx > len(all_alphabet)-1:
            new_idx = new_idx % len(all_alphabet)
        result += all_alphabet[new_idx]
    return result
        
            
        
    