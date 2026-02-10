function solution(s) {
    let result = 0;
    let cur_str_num = 0;
    let ant_str_num = 0;
    let cur_str = s[0]; 
    
    for(let i=0; i<s.length; i++) {
        if (cur_str !== s[i]) { 
            ant_str_num += 1; 
        } else {
            cur_str_num += 1;
        }
        
        if (cur_str_num === ant_str_num) {
            result += 1;
            cur_str_num = 0;
            ant_str_num = 0;
            
            if (i + 1 < s.length) {
                cur_str = s[i+1];
            }
        }
    }
    if (cur_str_num) result ++;
    return result;
}