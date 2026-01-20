def solution(ingredient):
    ham_stack = [] 
    result = 0
    
    for val in ingredient:
        ham_stack.append(val)
        if len(ham_stack) < 4: continue
        if val == 1 and ham_stack[-4:-1] == [1, 2, 3]:
            for i in range(4):
                ham_stack.pop()
            result += 1
                
    return result

