def solution(X, Y):
    num_lst = '9876543210'
    result = ''
    
    for i in num_lst:
        min_i_count = min(X.count(i), Y.count(i))
        for j in range(min_i_count):
            result += i
            
    if len(result) == 0: return '-1'
    if result[0] == '0': return '0'

    return result
