def solution(left, right):
    answer = 0
    
    # left 수 부터 right 수 까지의 범위 찾기
    for num in range(left, right + 1):
        # 공약수 구하기(제곱근 활용)
        common_divisor = []
    
    # 1. 일반적인 방법
        for i in range(1, num + 1):
            if num % i == 0:
                common_divisor.append(i)
        
        answer += num if len(common_divisor) % 2 == 0 else -num
    
    # 2. 시간 복잡도를 고려한 방법(일반 for문을 사용하는 것보다 1/2을 줄일 수 있다.)
#         for i in range(1, int(num ** (1 / 2)) + 1):
#             if num % i == 0:
#                 common_divisor.append(i)
#                 if i < num // i:
#                     common_divisor.append(num // i)
        
#         # 약수의 개수가 짝수면 더하기, 홀수면 빼기
#         answer += num if len(common_divisor) % 2 == 0 else -num
    
    return answer
