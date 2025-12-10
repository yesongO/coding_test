function solution(t, p) {
    let com_num = [];
    let com_len = t.length - p.length + 1;
    for(let i=0; i<com_len; i++) {
        com_num.push(Number(t.slice(i, i+p.length)));
    }
    let filtered = com_num.filter(i => i <= Number(p));
    return filtered.length;
}