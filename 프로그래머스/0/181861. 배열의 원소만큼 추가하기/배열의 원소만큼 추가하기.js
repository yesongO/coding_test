const solution = (arr) => {
    const result = []
    arr.forEach((i) => {
        for(let j=0; j<i; j++) {
            result.push(i);
        }
    })
    return result;
}