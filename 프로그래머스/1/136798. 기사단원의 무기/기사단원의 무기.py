# number: 숫자나라 기사단들의 번호
# limit: 공격력 제한 수치
# power: 제한 수치를 초과한 기사단의 무기 공격력

# ** 무기 공격력: 기사단 번호의 약수 개수

def solution(number, limit, power):
    answer = 0
    
    # 각 기사단 번호
    for num in range(1, number + 1):
        # 기사단의 번호를 기준으로 약수 구하기
        result = []
        for i in range(1, int(num**(1/2)) + 1):
            if num % i == 0:
                result.append(i)
                if i < num // i:
                    result.append(num // i)
            
        # 공격력 제한 수치보다 클 경우, 공격력이 power인 무기 구매
        answer += len(result) if len(result) <= limit else power
        
    return answer