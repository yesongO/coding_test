const solution = (binomal) => {
    const [a, op, b] = binomal.split(" ");
    
    switch(op) {
        case "+":
            return Number(a) + Number(b);
        case "-":
            return Number(a) - Number(b);
        case "*":
            return Number(a) * Number(b);
    }
}