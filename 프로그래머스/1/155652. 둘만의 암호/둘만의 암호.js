const solution = (s, skip, index) => {
    let alphabet_str = 'abcdefghijklmnopqrstuvwxyz';
    let alphabet_lst = alphabet_str.split('').filter((a) => !skip.includes(a));
    
    const alphabet_len = alphabet_lst.length;
    
    let result = '';
    
    s.split('').forEach((alphabet) => {
        let cur_index = alphabet_lst.indexOf(alphabet) + index;
        if (cur_index < alphabet_len) {
            result += alphabet_lst[cur_index];
        } else {
            result += alphabet_lst[cur_index % alphabet_len];
        }
    });
    return result;
}