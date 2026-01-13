def solution(n):
    n_to_three_reversed = ''
    while n > 0:
        n_to_three_reversed += str(n % 3)
        n = n // 3
    result = 0
    for i in range(len(n_to_three_reversed)): 
        result += (3**i) * int(n_to_three_reversed[len(n_to_three_reversed)-1-i]) 
    return result
