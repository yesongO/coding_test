def solution(my_string, alp):
    result = ""
    for s in my_string:
        if s == alp:
            result += s.upper()
        else:
            result += s
    return result