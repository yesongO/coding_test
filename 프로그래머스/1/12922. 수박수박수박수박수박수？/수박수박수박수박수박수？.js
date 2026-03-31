const solution = (n) => {
    const my_arr = ['수', '박'];
    let result = '';
    
    for (let i=0; i<n; i++) {
        if (i % 2 === 0) {
            result += my_arr[0];
        } else {
            result += my_arr[1];
        }
    }
    return result;
}