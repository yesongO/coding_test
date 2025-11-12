def solution(arr, queries):
    
    for q in queries:
        a, b = arr[q[0]], arr[q[1]]
        arr[q[0]] = b
        arr[q[1]] = a
        
    return arr