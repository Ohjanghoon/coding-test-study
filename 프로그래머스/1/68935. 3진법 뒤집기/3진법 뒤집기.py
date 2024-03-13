def solution(n):
    answer = 0
    
    answer = ''

    while n > 0:
        # 몫과 나머지를 튜플로 리턴
        n, re = divmod(n, 3)
        answer += str(re)
    return int(answer, 3) # int(수, n진법): n진법의 수를 10진수로 바꿔줌
