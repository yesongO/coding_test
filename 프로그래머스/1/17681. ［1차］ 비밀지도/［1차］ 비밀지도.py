def solution(n, arr1, arr2):
    map_1 = [bin(i)[2:].zfill(n) for i in arr1] #['01001', '10100', '11100', '10010', '01011']
    map_2 = [bin(i)[2:].zfill(n) for i in arr2] #['11110', '00001', '10101', '10001', '11100']
    
    result = [''] * n  #['', '', '', '', '']
    
    for i in range(n): # 0 1 2 3 4
        for j in range(n): # 0 1 2 3 4
            if map_1[i][j] + map_2[i][j] in ('01', '10', '11'):
                result[i] += '#'
            else:
                result[i] += ' '
                
    return result