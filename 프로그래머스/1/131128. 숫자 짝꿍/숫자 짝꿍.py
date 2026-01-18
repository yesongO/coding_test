def solution(X, Y):
    all_num = '9876543210'
    result = ''
    for num in all_num: # 이때 num은 문자열 ex) '9'
        min_count = min(X.count(num), Y.count(num))
        for i in range(min_count):
            result += num
    
    if len(result) == 0: return '-1'
    if result[0] == '0': return '0'
    
    return result