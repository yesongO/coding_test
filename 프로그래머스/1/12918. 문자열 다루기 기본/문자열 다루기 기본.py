def solution(s):
    str_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if len(s) != 4 and len(s) != 6:
        return False
    for str in s:
        if str not in str_list:
            return False
    return True
        