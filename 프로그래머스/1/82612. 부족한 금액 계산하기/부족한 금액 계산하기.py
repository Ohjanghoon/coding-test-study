def solution(price, money, count):
    answer = 0
    total_price = 0
    
    # 총 금액 구하기
    for i in range(1, count + 1):
        total_price += price * i
    
    # 얼마 모자라는지 구하기
    if total_price > money:
        answer = total_price - money
        
    return answer