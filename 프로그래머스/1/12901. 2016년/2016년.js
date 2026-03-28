const solution = (a, b) => {
    const month_day_lst = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    const day_lst = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED'];
    
    let acc_day = b;
    for (let i=0; i<a-1; i++) {
        acc_day += month_day_lst[i];
    }
    return day_lst[acc_day % 7];
}

// 날짜 합에서 7로 나눴을 때 나머지가 1:금 2:토 3:일 ...
