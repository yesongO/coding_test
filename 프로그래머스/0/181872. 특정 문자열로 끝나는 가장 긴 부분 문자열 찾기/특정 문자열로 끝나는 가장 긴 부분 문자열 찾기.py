def solution(myString, pat):
    end_idx = myString.rfind(pat[-1])
    return myString[:end_idx+1]