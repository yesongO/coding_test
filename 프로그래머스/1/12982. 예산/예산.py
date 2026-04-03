def solution(d, budget):
    d.sort()
    result = 0
    while d and budget >= d[0]:
        budget -= d[0]
        d.pop(0)
        result += 1
    return result
    