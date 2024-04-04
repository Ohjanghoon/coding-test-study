def solution(n):
    answer = 0
    tmp = n
    
    while True:
        ori_count = bin(n)[2:].count("1")
        tmp += 1
        min_count = bin(tmp)[2:].count("1")
        
        if ori_count == min_count:
            answer = tmp
            break
    return answer