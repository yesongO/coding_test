const solution = (numbers) => {
    const result_set = new Set();
    
    numbers.forEach((num, idx) => {
        for (let i=0; i<idx; i++) {
            result_set.add(num + numbers[i]);
        }
    });
    return [...result_set].sort((a, b) => a - b);
}