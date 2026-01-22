def solution(a, b):
    month_day_lst = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week_day_lst = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    
    day_sum = 0
    for i in range(a-1):
        day_sum += month_day_lst[i]
    day_sum += b
    
    return week_day_lst[day_sum % 7]


