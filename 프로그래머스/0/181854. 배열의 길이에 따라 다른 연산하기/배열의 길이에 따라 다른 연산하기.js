const solution = (arr, n) => {
    if (arr.length % 2 !== 0) {
        return arr.map((i, idx) => idx % 2 === 0 ? i + n : i);
    } else {
        return arr.map((i, idx) => idx % 2 !== 0 ? i + n : i);
    }
}