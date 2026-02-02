const solution = (strArr) => {
    const count = Array(31).fill(0);
    strArr.forEach((str) => {
        count[str.length] += 1;
    });
    return Math.max(...count);
}
