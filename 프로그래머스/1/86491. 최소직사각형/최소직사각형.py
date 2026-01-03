def solution(sizes):
    max_w = 0
    max_h = 0

    for w, h in sizes:
        big_side = max(w, h)
        small_side = min(w, h)
        max_w = max(max_w, big_side)
        max_h = max(max_h, small_side)

    return max_w * max_h
    
    
    
