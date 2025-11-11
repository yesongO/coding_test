def solution(numLog):
    result = ''
    my_dict = {1:'w', -1:'s', 10:'d', -10:'a'}
    
    for i in range(len(numLog)-1):
        num = numLog[i+1] - numLog[i]
        result += my_dict[num]

    return result