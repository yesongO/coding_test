def solution(s):
    s_mid = len(s) // 2
    if len(s) % 2 != 0:
        return s[s_mid]
    else:
        return s[s_mid-1:s_mid+1]