def solution(intStrs, k, s, l):
    cut = []
    answer = []
    for a in intStrs:
        cut.append(a[s:(s+l)])
    for i in cut:
        if int(i) > k:
            answer.append(int(i))
    return answer