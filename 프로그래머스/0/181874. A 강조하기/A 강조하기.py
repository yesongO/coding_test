def solution(myString):
    result = ""
    for s in myString:
        if s == "a":
            result += "A"
        elif s.upper() and s != "A":
            result += s.lower()
        else:
            result += s
    return result