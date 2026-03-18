def solution(n, words):
    acc_words = set()
    turn = 0
    
    for i in range(len(words)):
        if i % n == 0:
            turn += 1
        cur_order = i % n + 1
        
        if i >= 1 and words[i-1][-1] != words[i][0]:
            return [cur_order, turn]
        
        if words[i] not in acc_words:
            acc_words.add(words[i])
        else:
            return [cur_order, turn]
    
    return [0, 0]