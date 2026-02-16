def solution(babbling):
    can_speak_lst = ['aya', 'ye', 'woo', 'ma']
    result = 0
    
    for s in babbling:
        prev_c = ''
        
        while len(s) > 0:
            matched = False
            for c in can_speak_lst:
                if s.startswith(c) and prev_c != c:
                    s = s[len(c):]
                    prev_c = c
                    matched = True
                    break
                    
            if not matched:
                break;
        
        if s == '': result += 1       
    return result
                
            