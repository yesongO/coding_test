def solution(arr):
    two_idx = [] #[1, 5] .. [1] .. [1, 3, 6]
    for idx, i in enumerate(arr):
        if i == 2: two_idx.append(idx)
    if len(two_idx) == 0:
        return [-1]
    elif len(two_idx) == 1:
        return [arr[two_idx[0]]]
    else:
        return arr[two_idx[0]:two_idx[-1]+1]
