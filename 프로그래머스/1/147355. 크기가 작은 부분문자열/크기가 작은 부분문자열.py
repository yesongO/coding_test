def solution(t, p):
    com_len = len(t) - len(p) + 1
    com_lst = []
    for i in range(com_len):
        com_lst.append(int(t[i:i+len(p)]))
    com_lst = [j for j in com_lst if j <= int(p)]
    return len(com_lst)
        