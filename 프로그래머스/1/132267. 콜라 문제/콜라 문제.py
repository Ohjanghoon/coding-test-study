# a, b: 빈병 a개를 가져다주면 콜라 b병
# n: 가지고 있는 빈 병수

def solution(a, b, n):
    answer = 0
    
    while True:
        if n < a:
            break

        x, y = divmod(n, a)
        answer += x * b
        n = x * b + y
        
    return answer