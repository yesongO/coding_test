const solution = (price, money, count) => {
    let require_money = 0;
    for (let i=1; i<count+1; i++) {
        require_money += price * i; 
    }
    return money >= require_money ? 0 : (require_money - money); 
}