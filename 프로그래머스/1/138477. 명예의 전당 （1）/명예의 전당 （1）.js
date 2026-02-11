const solution = (k, score) => {
    const result = [];
    const cur_score = [];
    score.forEach((i, idx) => {
        cur_score.push(i);
        if (idx < k) { result.push(Math.min(...cur_score)) }
        else {
            cur_score.sort((a, b) => b - a);
            result.push(cur_score[k-1]);
        }
    });
    return result;
}