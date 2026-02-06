const solution = (cards1, cards2, goal) => {
    let check_num = 0;
    goal.forEach((str) => {
        if (cards1 && cards1[0] === str) {
            cards1.shift();
            check_num ++;
        } else if (cards2 && cards2[0] === str) {
            cards2.shift();
            check_num ++;
        }
    });
    return check_num === goal.length ? "Yes" : "No";
}