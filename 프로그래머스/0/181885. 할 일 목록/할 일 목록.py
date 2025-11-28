def solution(todo_list, finished):
    result = []
    for idx, v in enumerate(finished):
        if v == False:
            result.append(todo_list[idx])
    return result