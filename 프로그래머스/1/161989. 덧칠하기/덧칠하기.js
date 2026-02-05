const solution = (n, m, section) => {
    painting_arr = Array(n).fill(1);
    section.forEach((i) => painting_arr[i-1] = 0);
    
    let result = 0;
    let cur_idx = 0;
    
    while (cur_idx < n) {
        if (painting_arr[cur_idx] === 0) {
            result += 1;
            cur_idx += m;
        } else {
            cur_idx += 1;
        }
    }
    return result;
}