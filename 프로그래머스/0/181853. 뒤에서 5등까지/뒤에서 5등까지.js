const solution = (num_list) => {
    const result = [];
    for (let i=0; i<5; i++) {
        const min_num_list = Math.min(...num_list);
        result.push(min_num_list);
        num_list.splice(num_list.indexOf(min_num_list), 1);
    }
    return result;
}