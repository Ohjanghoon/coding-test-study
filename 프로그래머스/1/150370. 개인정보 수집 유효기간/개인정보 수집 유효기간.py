# 모든 달은 28일까지 있다고 가정
# today: 오늘 날짜 <문자열> => YYYY.MM.DD
# terms: 약관의 유효기간 <1차원 배열> => ["{약관 종류} {유효기간}"]
# ㄴ 약관 종류: 중복되지 않은 A ~ Z
# ㄴ 유효기간: 1 ~ 100
# privacies: 수집된 개인정보 담은 <1차원 배열>
# return - 파기해야 할 개인정보 번호 오름차순 정렬
def solution(today, terms, privacies):
    answer = []
    
    t_year, t_month, t_day = [int(t) for t in today.split('.')]
    
    term_dict = {}
    for term in terms:
        key, value = term.split(' ')
        term_dict[key] = int(value)
    
    for idx, p in enumerate(privacies):
        date, term = p.split(' ')
        year, month, day = [int(d) for d in date.split('.')]
        
        plus_month = term_dict[term]
        month += plus_month

        while month > 12:
            year += 1
            month -= 12
    
        print(t_year, t_month, t_day)
        print(year, month, day)
        # 년도 비교
        if t_year > year:
            answer.append(idx + 1)
        elif t_year == year:
            # 월 비교
            if t_month > month:
                answer.append(idx + 1)
            # 일 비교
            elif t_month == month:
                if t_day >= day:
                    answer.append(idx + 1)        
        
    return answer