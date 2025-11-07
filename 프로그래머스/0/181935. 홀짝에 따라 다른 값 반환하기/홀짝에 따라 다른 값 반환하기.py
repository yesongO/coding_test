def solution(n):
    answer = 0
    
    if n % 2 != 0: # n이 홀수일때
        while (n >= 0):
            answer += n
            n = n-2

    else: # n이 짝수일때
        while (n > 0):
            answer += n**2
            n = n-2
            
    return answer