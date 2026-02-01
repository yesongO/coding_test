const solution = (arr) => {
    const num_lst = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024];
    const result = [...arr];
    
    for (const num of num_lst) {
        if (result.length === num) return result;
        if (result.length < num) {
            while (result.length < num) {
                result.push(0);
            }
            return result;
        } 
    }
}