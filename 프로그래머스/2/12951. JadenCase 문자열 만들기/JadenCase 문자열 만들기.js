const solution = (s) => {
    return s
        .split(" ")
        .map((word) => {
            if (word === "") {
                return "";
            } else {
                return word[0].toUpperCase() + word.slice(1).toLowerCase();
            }
        }).join(" ");
}