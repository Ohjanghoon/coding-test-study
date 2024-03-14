def solution(d, budget):
    answer = 0
    
    d.sort()
    if budget == sum(d):
        answer = len(d)
    else:
        for price in d:
            budget -= price
            if budget < 0:
                break
            answer += 1 
    
    return answer