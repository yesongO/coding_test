function solution(k, score) {
    let result = [];
    let acc = [];
    for (let i=0; i<score.length; i++) {
        acc.push(score[i]);
        if (i < k) {
            result.push(Math.min(...acc));
        } else {
            result.push([...acc].sort((a, b) => b - a)[k-1]);
        }
    }
    return result;
}