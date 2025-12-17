function solution(food) {
    let one_side = "";
    for(let i=1; i<food.length; i++) {
        one_side += String(i).repeat(Math.floor(food[i] / 2));
    }
    return one_side + "0" + one_side.split("").reverse().join("");
}