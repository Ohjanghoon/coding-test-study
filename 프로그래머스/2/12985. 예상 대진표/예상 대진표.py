# 1, 2 > 1 > 1 > 1
# 3, 4 > 2 > 1 > 1
# 5, 6 > 3 > 2 > 1
# 7, 8 > 4 > 2 > 1

def solution(n,a,b):
    answer = 0

    while a != b:
        a = int((a + 1) / 2)
        b = int((b + 1) / 2)
        answer += 1
        
    return answer
        