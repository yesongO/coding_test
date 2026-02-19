const solution = (X, Y) => {
    const count_X = Array(10).fill(0);
    const count_Y = Array(10).fill(0);
    
    for (const x of X) { count_X[x] ++; }
    for (const y of Y) { count_Y[y] ++; }
    
    let result = ''
    for (let i=9; i>-1; i--) {
        const cur_count = Math.min(count_X[i], count_Y[i]);
        result += String(i).repeat(cur_count);
    }
    if (result[0] === '0') { return '0'; }
    return !result ? '-1' : result;
}