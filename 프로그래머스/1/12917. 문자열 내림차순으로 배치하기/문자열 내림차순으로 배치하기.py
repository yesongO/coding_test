def solution(s):
    s_sort_arr = sorted(s, reverse=True)
    return "".join(s_sort_arr)