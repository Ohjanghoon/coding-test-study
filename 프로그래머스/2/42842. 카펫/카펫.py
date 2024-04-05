def solution(brown, yellow):
    answer = []
    width = 0
    height = 0
    
    result = []
    for i in range(1, int(yellow ** (1/2)) + 1):
        tmp = []
        if yellow % i == 0:
            tmp.append(i)
            if i < yellow // i:
                tmp.append(yellow // i)
        
        if tmp != []:
            result.append(tmp)
    
    CORNER = 4
    up_down = 1
    left_right = 1
    
    
    for res in result:
        if len(res) == 1:
            left_right *= res[0] * 2
            up_down *= res[0] * 2
        else:
            left_right *= res[0] * 2
            up_down *= res[1] * 2
            
        if CORNER + up_down + left_right == brown:
            return [up_down / 2 + 2, left_right / 2 + 2]
        else:
            left_right = 1
            up_down = 1
            
            
    return answer