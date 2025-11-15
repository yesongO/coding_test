def solution(number):
    sum_num = 0
    for i in str(number):
        sum_num += int(i)
    return sum_num % 9