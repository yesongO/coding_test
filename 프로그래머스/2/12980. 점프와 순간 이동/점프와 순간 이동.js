const solution = (n) => {
    let result = 1
    
    while (n != 1) {
        if (n % 2 === 0) {
            n = Math.floor(n / 2);
        } else {
            result += 1
            n -= 1
        }
    }
    return result;
}