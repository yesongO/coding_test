const solution = (s) => {
    const result = [];
    const my_dict = {};
    
    s.split('').forEach((str, idx) => {
        if (my_dict[str] === undefined) {
            result.push(-1);
        } else {
            result.push(idx - my_dict[str]);
        }
        my_dict[str] = idx;
    });
    return result;
}