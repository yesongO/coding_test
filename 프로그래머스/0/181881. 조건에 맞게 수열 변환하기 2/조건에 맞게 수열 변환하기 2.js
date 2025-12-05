function solution(arr) {
    let prv = [...arr];
    let result = 0;
    while (true) {
        let nxt = []
        for (let i=0; i<prv.length; i++) {
            if (prv[i] >= 50 && prv[i] % 2 === 0) {
                nxt.push(Math.floor(prv[i] / 2));
            } else if (prv[i] < 50 && prv[i] % 2 !== 0) {
                nxt.push(prv[i] * 2 + 1);
            } else {
                nxt.push(prv[i]);
            }
        }
        if (JSON.stringify(prv) === JSON.stringify(nxt)) { break }
        prv = [...nxt];
        result += 1;
    }
    return result;
}