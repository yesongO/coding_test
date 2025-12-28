function solution(s) {
    if (s.length !== 4 && s.length !== 6) return false;
    return s
        .split("")
        .map(v => "0123456789".includes(v))
        .every(v => v === true);
}