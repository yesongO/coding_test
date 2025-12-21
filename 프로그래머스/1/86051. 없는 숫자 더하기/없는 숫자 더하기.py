def solution(numbers):
    no_num_list = []
    for i in range(0, 10):
        if i not in numbers:
            no_num_list.append(i)
    return sum(no_num_list)