function solution(s) {
    let result = [];
    for (let i=0; i<s.length; i++) { 
        let cur_str = s[i];
        let found = false;
        for (let j=i-1; j>-1; j--) { 
            if (s[j] === cur_str) {
                result.push(i-j);
                found = true;
                break;
            }
        }
        if (!found) {
            result.push(-1);
        }
    }
    return result;
}