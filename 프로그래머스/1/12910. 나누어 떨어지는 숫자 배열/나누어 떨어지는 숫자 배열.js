function solution(arr, divisor) {
    const result_arr = arr
        .filter(v => v % divisor === 0)
        .sort((a, b) => a - b);
    return result_arr.length === 0 ? [-1] : result_arr;
}