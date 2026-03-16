def solution(s):
    my_stack = [s[0]]
    
    for i in range(1, len(s)):
        my_stack.append(s[i])
        if len(my_stack) >= 2 and my_stack[-1] == my_stack[-2]:
            for i in range(2): my_stack.pop()
            
    return 0 if my_stack else 1