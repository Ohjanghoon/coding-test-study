# 장군개미(5), 병정개미(3), 일개미(1)

def solution(hp):
    answer = 0
    ants_attack = [5, 3, 1]
    ants = [] 
    
    for idx, ant in enumerate(ants):
        if hp != 0:
            n, hp = divmod(hp, ant)
            ants.append(n)
        else:
            break
        
        
    print(ants)
    return answer