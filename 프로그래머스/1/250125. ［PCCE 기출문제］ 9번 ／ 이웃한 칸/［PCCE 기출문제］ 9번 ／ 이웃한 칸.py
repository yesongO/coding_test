def solution(board, h, w):
    board_len = len(board)
    result = 0
    
    dh = [1, 0, -1, 0]
    dw = [0, 1, 0, -1]
    
    for i in range(4):
        cur_color = board[h][w]
        h_check, w_check = h + dh[i], w + dw[i]
        if (0 <= h_check < board_len and 0 <= w_check < board_len):
            if board[h_check][w_check] == cur_color:
                result += 1
                
    return result