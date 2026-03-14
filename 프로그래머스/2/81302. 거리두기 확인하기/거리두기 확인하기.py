def solution(places):
    result = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for i in range(5):
        cur_place = [list(s) for s in places[i]]
        violation = False
        
        for r in range(5):
            if violation: break
            for c in range(5):
                if cur_place[r][c] != "P":
                    continue
                
                # P인 경우 동서남북 탐색
                for d in range(4):
                    new_x, new_y = r + dx[d], c + dy[d]
                    if not (0 <= new_x < 5 and 0<= new_y < 5):
                        continue
                    
                    if cur_place[new_x][new_y] == "P":
                        violation = True
                        break
                    
                    if cur_place[new_x][new_y] == "O":
                        for dd in range(4):
                            new_xx, new_yy = new_x + dx[dd], new_y + dy[dd]
                            if not (0 <= new_xx < 5 and 0<= new_yy < 5):
                                continue
                            if new_xx == r and new_yy == c:
                                continue
                            if cur_place[new_xx][new_yy] == "P":
                                violation = True
                                break
                        if violation:
                            break
                if violation:
                    break
                        
        result.append(0 if violation else 1)
    return result

                        
'''
맨해튼 거리 (r1, c1), (r2, c2) => |r1 - r2| + |c1 - c2|

해당 자리가 P일 경우 
1. 동서남북 중 하나라도 P면 0 반환
2. 동서남북 중 하나가 O 라면
    2-1 온 방향을 제외한 동서남북 중 하나라도 P면 0 반환
'''
