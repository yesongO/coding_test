def solution(code):  # code는 소문자 또는 1로 구성된 문자열
    ret = ''
    cur_mode = 0
    
    for idx in range(len(code)):
        if cur_mode == 0: # 현재 모드가 0일 경우
            if code[idx] == "1": # "1" 일 경우 모드 바꾸기
                cur_mode = 1
            elif idx % 2 == 0: # idx가 짝수일 경우
                ret += code[idx]
                
        else: # 현재 모드가 1일 경우
            if code[idx] == "1": # "1" 일 경우 모드 바꾸기
                cur_mode = 0
            elif idx % 2 != 0:
                ret += code[idx]
    
    if ret == '':
        return "EMPTY"
            
    return ret