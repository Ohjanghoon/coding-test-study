def solution(s):
    answer = 0
    first = ''
    first_count = 0
    other_count = 0
    
    for idx, alpha in enumerate(s):
        if first == '':
            first = alpha
            first_count += 1
        else:
            if first == alpha:
                first_count += 1
            else:
                other_count += 1
        
        if idx == len(s) - 1 or first_count == other_count:
            answer += 1
            first = ''
                
        
            
        
    return answer