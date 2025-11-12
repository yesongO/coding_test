def solution(arr, queries):
    answer = []
    for a, b, c in queries:
        val = -1
        new_list = arr[a:b+1]
        for i in new_list:
            if i > c:
                if val == -1:
                    val = i
                elif i < val: 
                    val = i
        answer.append(val)
    return answer