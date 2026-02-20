def solution(survey, choices):
    mbti_dic = { 'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0 }
    result = ''
    
    for i in range(len(survey)):
        first, second = survey[i][0], survey[i][1]  # 'A', 'N'
        if choices[i] == 1:
            mbti_dic[first] += 3
        elif choices[i] == 2:
            mbti_dic[first] += 2
        elif choices[i] == 3:
            mbti_dic[first] += 1
        elif choices[i] == 5:
            mbti_dic[second] += 1
        elif choices[i] == 6:
            mbti_dic[second] += 2
        elif choices[i] == 7:
            mbti_dic[second] += 3
            
    result += 'R' if mbti_dic['R'] >= mbti_dic['T'] else 'T'
    result += 'C' if mbti_dic['C'] >= mbti_dic['F'] else 'F'
    result += 'J' if mbti_dic['J'] >= mbti_dic['M'] else 'M'
    result += 'A' if mbti_dic['A'] >= mbti_dic['N'] else 'N'
    
    return result


# 매우비동의(1) / 비동의(2) / 약간비동의(3) / 몰라(4) / 약간동의(5) / 동의(6) / 매우동의(7)
#    3            2         1            0        1           2       3

# 점수가 같으면 사전순

# 1번지표 : R / T
# 2번지표 : C / F
# 3번지표 : J / M
# 4번지표 : A / N

# survey[i] -> A(비동의) B(동의)