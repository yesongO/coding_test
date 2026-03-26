const solution = (s) => {
    const my_stack = [];
    
    for (const alphabet of s) {
        my_stack.push(alphabet);
        let stack_length = my_stack.length;
        if (stack_length > 1 && my_stack[stack_length-1] === my_stack[stack_length - 2]) {
            my_stack.pop();
            my_stack.pop();
        }
    };
    return my_stack.length === 0 ? 1 : 0; 
}