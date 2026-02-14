const solution = (k, m, score) => {
    const score_queue = score.sort((a, b) => b - a);
    const result = [];
    let pointer = 0;
    
    while (pointer <= score_queue.length-m) {
        const cur_store_lst = [];
        for (let i=0; i<m; i++) {
            cur_store_lst.push(score_queue[pointer]);
            pointer ++;
        }
        result.push(Math.min(...cur_store_lst) * m);
    }
    return result.reduce((acc, cur) => acc + cur, 0);
}