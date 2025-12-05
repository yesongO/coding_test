def solution(arr):
    prv = arr[:]
    x = 0
    while True:
        nxt = []
        for i in prv:
            if i >= 50 and i % 2 == 0:
                nxt.append(i // 2)
            elif i < 50 and i % 2 != 0:
                nxt.append(i * 2 + 1)
            else:
                nxt.append(i)
        if prv == nxt:
            break
        prv = nxt[:]
        x += 1
    return x