# 체력 회복: t초 * x체력
# 연속 체력 회복: t초 * x체력 + y추가체력
# 단, 체력은 최대 체력(health)보다 커지는 건 불가.

# 공격: 기술 취소, 회복 x => 연속 성공 0 초기화
# 공격: 체력 - 피해량
# 체력 <= 0: 캐릭 죽음, 체력 회복x ==> -1 리턴

# bandage: [기술 시간(t), 초당 회복량(x), 추가 회복량(y)]
# health: 최대 체력
# attacks: [[공격 시간, 피해량]]


def solution(bandage, health, attacks):
    # 공격 정보
    attack_dict = {}
    for attack in attacks:
        attack_dict[attack[0]] = attack[1]
    
    # 마지막 공격 시간
    attack_time = attacks[len(attacks) - 1][0]
    
    # 시전 시간, 초당 회복량, 추가 회복량
    t, x, y = bandage
    curr_health = health
    
    # 현재 시간(0은 의미가 없으므로, 1초부터 시작)
    curr_time = 1
    total_duration = 0
    while curr_time <= attack_time:
        # 공격
        if curr_time in attack_dict.keys():
            # 현재 체력 - 피해량
            curr_health -= attack_dict[curr_time]
            # 연속 성공 시간 초기화
            total_duration = 0
            # 공격 당한 후 체력이 없으면 사망
            if curr_health <= 0:
                return -1
        # 회복
        else:
            # 연속 성공 시간 증가
            total_duration += 1
            
            # 기본 체력 회복 
            curr_health += x

            # 최대 체력일 경우, 더 이상 회복 x
            if curr_health >= health:
                curr_health = health

            # 성공 시간이 시전 시간과 크거나 같을 경우 
            if total_duration >= t:
                # 추가 회복량
                curr_health += y
                if curr_health >= health:
                    curr_health = health
                # 연속 성공 시간 초기화
                total_duration = 0
                
        # print("curr_time ==> {}, curr_health ==> {}".format(curr_time, curr_health))
        # 시간 증가
        curr_time += 1
    
    return curr_health