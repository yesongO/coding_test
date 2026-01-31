const solution = (arr) => {
    const stk = [];
    arr.forEach((n, i) => {
        if (i === 0) {
            stk.push(n);
        } else if (stk && stk.at(-1) === n) {
            stk.pop();
        } else {
            stk.push(n);
        }
    });
    return stk.length === 0 ? [-1] : stk;
}