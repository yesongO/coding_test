const solution = (myStr) => {
    const my_str = myStr
        .split(/[abc]/)
        .filter((s) => s !== "");
    return my_str.length !== 0 ? my_str : ["EMPTY"];
}