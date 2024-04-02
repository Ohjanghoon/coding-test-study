# 알아볼 수 없는 번호 0으로 표기
# return - 당첨가능한 [최고 순위, 최저 순위]
# lottos: 민우가 구매한 로또 번호
# win_nums: 당첨번호
def solution(lottos, win_nums):
    
    win_count = 0
    secret_count = lottos.count(0)
    grade = [6, 6, 5, 4, 3, 2, 1]
    
    for lot in lottos:
        if lot in win_nums:
            win_count += 1

    print(win_count, win_count + secret_count)
    win_grade = grade[win_count:win_count + secret_count + 1]
    return [min(win_grade), max(win_grade)]