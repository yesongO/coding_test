def solution(board, h, w):
    n = len(board)
    count = 0
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    color = board[h][w]
    
    for i in range(4): 
        
        # 범위를 벗어날 경우
        if (h + dh[i] < 0 or h + dh[i] > n - 1 or w + dw[i] < 0 or w + dw[i] > n - 1):
            continue
                
        if board[h+dh[i]][w+dw[i]] == color:
            count += 1
            
    return count



