def solution(a, b):
    answer = ''
    month_to_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_of_week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    
    
    tmp = 0
    for month_idx in range(0, a - 1):
        tmp += month_to_day[month_idx]
    
    day_idx = (tmp + b - 1) % len(day_of_week)
    answer = day_of_week[day_idx]
    
    
    return answer