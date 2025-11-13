def solution(x1, x2, x3, x4):
    left, right, last = False, False, True
    if x1 == True or x2 == True:
        left = True
    if x3 == True or x4 == True:
        right = True
    if left == False or right == False:
        last = False
    return last