def solution(A,B):
    answer = 0
    asc_A, des_B = sorted(A), sorted(B, reverse=True)
    
    for i in range(len(A)):
        answer += asc_A[0] * des_B[0]
        asc_A.pop(0)
        des_B.pop(0)
        
    return answer