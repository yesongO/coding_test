const solution = (name, yearning, photo) => {
    const result = Array(photo.length).fill(0);
    const yearningObject = {};
    name.forEach((name, idx) => yearningObject[name] = yearning[idx]);
    
    photo.forEach((lst, idx) => {
        lst.forEach((name) => {
            result[idx] += yearningObject[name] ?? 0
        });
    });
    return result;
}