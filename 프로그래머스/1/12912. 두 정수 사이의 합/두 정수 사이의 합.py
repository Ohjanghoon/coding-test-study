def solution(a, b):
    answer = 0
    
    if a == b: return a
    
    min_num = a if a < b else b
    max_num = a if a > b else b


    for i in range(min_num, max_num + 1):
        answer += i        
        
    return answer