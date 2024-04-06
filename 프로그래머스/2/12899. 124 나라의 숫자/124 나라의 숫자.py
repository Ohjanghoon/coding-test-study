def solution(n):
    answer = ''
    ex_list = ['1', '2', '4']
    
    while n > 0:
        n -= 1
        n, idx = divmod(n, 3)
        answer = ex_list[idx] + answer
        
    return answer