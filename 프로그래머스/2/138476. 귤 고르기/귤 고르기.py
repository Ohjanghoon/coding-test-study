def solution(k, tangerine):
    answer = 0
    dict ={}
    
    for t in list(set(tangerine)):
        dict[t] = 0
    
    for t in tangerine:
        dict[t] += 1
        
    dict_list = sorted(dict.values(), key = lambda x: x, reverse=True)
    
    for i in dict_list:
        answer += 1
        if k - i > 0:
            k -= i        
        else:
            break
    return answer