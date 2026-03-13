def solution(n):
    result = 1
    
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            result += 1
            n -= 1
            
    return result

'''
k칸 점프 (k만큼 건전지 사용) / 현재거리 x 2 순간이동 (건전지 사용 안함)
'''