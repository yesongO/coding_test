const solution = (keymap, targets) => {
    const key_dict = {}
    
    keymap.forEach((keys) => {
        for(let i=0; i<keys.length; i++) {
            const cur_key = keys[i];
            key_dict[cur_key] = Math.min(key_dict[cur_key] ?? i + 1, i + 1);
        }
    });
    
    result = []
    
    targets.forEach((target) => {
        let total_sum = 0
        let can_make = true
        
        for (const s of target) {
            if (key_dict[s] === undefined) {
                result.push(-1);
                can_make = false;
                break;
            } else {
                total_sum += key_dict[s];
            }
        }
        if (can_make) { result.push(total_sum); }
    });
    return result;
} 