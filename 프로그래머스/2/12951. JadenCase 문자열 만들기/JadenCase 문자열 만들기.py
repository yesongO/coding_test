def solution(s):
    result = ''
    capital = True
    
    for a in s:
        if a == ' ':
            result += a
            capital = True
        elif a.isdigit():
            result += a
            capital = False
        else:
            if capital: 
                result += a.upper()
                capital = False
            else: 
                result += a.lower()
                
    return result
            
    