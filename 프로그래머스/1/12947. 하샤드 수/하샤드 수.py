def solution(x):
    num = 0
    for i in list(str(x)):
        num += int(i)
    
    answer = (x % num == 0)
    
    return answer