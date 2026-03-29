const solution = (absolutes, signs) => {
    let result = 0;
    
    absolutes.forEach((num, idx) => {
        const cur_num = signs[idx] === true ? num : -num
        result += cur_num;
    });
    
    return result;
}