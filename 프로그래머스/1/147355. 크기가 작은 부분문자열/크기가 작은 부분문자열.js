function solution(t, p) {
    const p_len = p.length;
    const split_num_lst = [];
    let result = 0;
    
    for (let i=0; i<t.length - p_len + 1; i++) {
        split_num_lst.push(Number(t.slice(i, i+p_len)));
    }
    
    split_num_lst.forEach((num) => {
        if (num <= Number(p)) {
            result += 1;
        }
    });
    return result;
}