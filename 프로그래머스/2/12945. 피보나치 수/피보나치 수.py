def solution(n):
    answer = 0
    fib_list = [0, 1]
    fib_idx = 0
    
    for i in range(2, n + 1):
        fib_list.append(fib_list[i - 2] + fib_list[i - 1])
    
    answer = fib_list[n] % 1234567
    return answer