from itertools import combinations

def solution(number):
    result = 0
    for com in combinations(number, 3):
        if sum(com) == 0:
            result += 1
    return result
