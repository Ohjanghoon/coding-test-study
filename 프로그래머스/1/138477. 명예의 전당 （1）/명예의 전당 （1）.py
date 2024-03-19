def solution(k, score):
    answer = []
    honor_list = []
    
    for num in score:
        if len(honor_list) < k:
            honor_list.append(num)
        else:
            if num >= min(honor_list):
                del honor_list[0]
                honor_list.append(num)
            
        answer.append(min(honor_list))
        honor_list.sort()
        
    return answer