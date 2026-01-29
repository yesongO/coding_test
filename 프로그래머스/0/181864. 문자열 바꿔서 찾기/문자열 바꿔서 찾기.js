const solution = (myString, pat) => {
    const my_string = myString.split("").map((s) => s === "A"?"B":"A").join("");
    return my_string.includes(pat) ? 1 : 0;
}