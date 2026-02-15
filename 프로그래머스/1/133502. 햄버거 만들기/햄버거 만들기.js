const solution = (ingredient) => {
    const ingredient_stack = [];
    let result = 0;
    ingredient.forEach((i) => {
        ingredient_stack.push(i);
        if (ingredient_stack.length >= 4) {
            if (ingredient_stack.slice(-4).join('') === '1231') {
                for (let i=0; i<4; i++) {
                    ingredient_stack.pop();
                }
                result += 1;
            }
        }
    });
    return result;
}