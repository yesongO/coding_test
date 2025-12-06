def solution(myString, pat):
    myString_ = myString.upper()
    pat_ = pat.upper()
    if pat_ in myString_:
        return 1
    else:
        return 0