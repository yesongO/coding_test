const solution = (arr1, arr2) => {
    const arr1_length = arr1.length;
    const arr2_length = arr2.length;
    
    const arr1_sum = arr1.reduce((acc, cur) => acc + cur, 0);
    const arr2_sum = arr2.reduce((acc, cur) => acc + cur, 0);
    
    if (arr1_length === arr2_length) {
        if (arr1_sum === arr2_sum) return 0;
        return arr1_sum > arr2_sum ? 1 : -1;
    }
    return arr1_length > arr2_length ? 1 : -1;
}