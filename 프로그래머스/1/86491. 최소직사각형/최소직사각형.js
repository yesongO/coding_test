const solution = (sizes) => {
    let width = 0;
    let height = 0;
    
    sizes.forEach((lst) => {
        let large_side = Math.max(...lst);
        let small_side = Math.min(...lst);
        width = Math.max(width, large_side);
        height = Math.max(height, small_side);
    });
    return width * height;
}