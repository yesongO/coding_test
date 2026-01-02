function solution(s) {
    const s_len = s.length;
    if (s_len % 2 !== 0) {
        return s[Math.floor(s_len / 2)];
    } else {
        return s.slice(s_len / 2 - 1, s_len / 2 + 1);
    }
}