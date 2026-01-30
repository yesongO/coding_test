const solution = (arr, flag) => {
    const result = [];
    flag.forEach((v, i) => {
        if (v) {
            for(let j=0; j<arr[i]*2; j++) {
                result.push(arr[i]);
            }
        } else {
            for(let k=0; k<arr[i]; k++) {
                result.pop();
            }
        }
    })
    return result;
}