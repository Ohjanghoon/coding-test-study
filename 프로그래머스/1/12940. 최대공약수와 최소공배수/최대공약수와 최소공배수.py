def solution(n, m):
    answer = []
    
    # 최대공약수: 작은 수부터 0까지 하나씩 나눠서 구하기
    for i in range(min(n, m), 0, -1):
        if (n % i == 0) and (m % i == 0):
            gcd_num = i
            break
    
    # 최소공배수
    for j in range(max(n, m), (n * m) + 1):
        if (j % n == 0) and (j % m == 0):
            lcm_num = j
            break
    
    answer = [gcd_num, lcm_num]
    return answer