def solution(s):
    if s[0] == ')': return False

    my_stack = []
    for val in s: 
        if val == '(':
            my_stack.append(val)
        else:
            if len(my_stack) == 0:
                return False
            elif my_stack[-1] == '(': 
                my_stack.pop()
            else:
                my_stack.append(val)

    if len(my_stack) == 0: 
        return True 
    else: 
        return False
