def solution(n):
    
    # 2번째 시도(에라토스테네스의 체)
    a = [False,False] + [True]*(n-1)
    primes=[]

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False
    
    answer = len(primes)
    
    # 1번째 시도(시간 초과)
#     for i in range(2, n + 1):
#         if isinstance(i ** 1/2, int):
#             continue
            
#         for j in range(2, int(i ** 1/2) + 1):
#             if i % j == 0:
#                 break
#         else:
#             answer += 1
            
            
    return answer