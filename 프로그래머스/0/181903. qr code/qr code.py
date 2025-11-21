def solution(q, r, code):
    result = ""
    for i in range(len(code)): # 0, 1, 2, ..., 16
        if i % q == r:
            result += code[i]
    return result