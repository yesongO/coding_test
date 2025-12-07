function solution(myString, pat) {
    const end_idx = myString.lastIndexOf(pat[pat.length - 1]);
    return myString.slice(0, end_idx+1);
}