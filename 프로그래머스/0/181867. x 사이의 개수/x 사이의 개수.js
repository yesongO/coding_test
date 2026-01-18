function solution(myString) {
    new_split_arr = myString.split('x')
    return new_split_arr.map((str) => str.length);
}