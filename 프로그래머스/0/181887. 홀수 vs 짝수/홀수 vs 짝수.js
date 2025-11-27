function solution(num_list) {
    let odd_add = 0;
    let even_add = 0;
    for(let i=0; i<num_list.length; i+=2) {
        odd_add += num_list[i];
    }
    for(let i=1; i<num_list.length; i+=2) {
        even_add += num_list[i];
    }
    return Math.max(odd_add, even_add);
}