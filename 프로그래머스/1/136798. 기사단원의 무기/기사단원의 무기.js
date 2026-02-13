const solution = (number, limit, power) => {
    let result = 0;
    const divisor_lst = Array(number + 1).fill(0); 
    for (let i=1; i<number+1; i++) { 
        for (let j=i; j<number+1; j+=i) { 
            divisor_lst[j] += 1;
        }
    }
    divisor_lst.forEach((num) => {
        if (num <= limit) {
            result += num;
        } else {
            result += power;
        }
    });
    return result;
}