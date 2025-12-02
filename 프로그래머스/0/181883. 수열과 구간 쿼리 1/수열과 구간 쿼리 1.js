function solution(arr, queries) {
    for (let i=0; i<queries.length; i++) {
        let s = queries[i][0];
        let e = queries[i][1];
        
        for (let i=s; i<e+1; i++) {
            arr[i] += 1;
        }
    }
    return arr;
}