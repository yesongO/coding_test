function solution(A,B){
    let answer = 0;
    A.sort((a, b) => a - b);
    B.sort((a, b) => b - a);
    
    A.forEach((v, i) => {
        answer += v * B[i]
    });
    return answer;
}

/*
A는 오름차순 정렬, B는 내림차순 정렬
n번째 위치씩 각각 곱하여 더하기
*/