function solution(myString) {
    return myString
        .split('')
        .map((v) => 'abcdefghijk'.includes(v) ? 'l' : v)
        .join('')
}
