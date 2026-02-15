def solution(ingredient):
    my_stack = [] 
    result = 0
    
    for i in ingredient:
        my_stack.append(i)     
        if len(my_stack) < 4: continue
        if i == 1 and my_stack[-4:] == [1, 2, 3, 1]:
            for j in range(4):
                my_stack.pop()
            result += 1
    return result
    
            