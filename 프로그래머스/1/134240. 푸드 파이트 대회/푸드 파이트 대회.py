def solution(food):
    answer = ''
    tmp = ''
    for idx in range(1, len(food)):
        if food[idx] // 2 > 0:
            tmp += str(idx) * (food[idx] // 2)
    
    rev_tmp = ''.join(reversed(tmp))
    answer = tmp + "0" + rev_tmp
    
    return answer