def solution(s):
    word_list = s.split(" ")
    result = []
    for str in word_list:
        new_word = ""
        for i in range(len(str)): 
            if i % 2 == 0:
                new_word += str[i].upper()
            else:
                new_word += str[i].lower()
        result.append(new_word)
    return " ".join(result)