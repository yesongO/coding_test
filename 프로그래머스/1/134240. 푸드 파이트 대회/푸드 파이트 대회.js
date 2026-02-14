const solution = (food) => {
    let half_result = '';
    food.forEach((i, idx) => {
        if (idx !== 0) {
            half_result += String(idx).repeat(Math.floor(i / 2));
        }
    });
    return half_result + '0' + half_result.split('').reverse().join('');
}