def solution(num_list):
    odd_add = 0
    even_add = 0
    for i in range(1, len(num_list)+1):
        if i % 2 != 0:
            odd_add += num_list[i-1]
        else:
            even_add += num_list[i-1]
    return max(odd_add, even_add)  