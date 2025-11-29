function solution(numbers, n) {
    let total = 0;
    for (let i=0; i<numbers.length; i++) {
        total += numbers[i];
        if (total > n) {
            return total;
        }
    }
}