function solution(cards1, cards2, goal) {
    for (let i=0; i<goal.length; i++) {
        let s = goal[i];
        if (cards1 && cards1[0] === s) {
            cards1.shift();
        } else if (cards2 && cards2[0] === s) {
            cards2.shift();
        } else {
            return "No";
        }
    }
    return "Yes";
}