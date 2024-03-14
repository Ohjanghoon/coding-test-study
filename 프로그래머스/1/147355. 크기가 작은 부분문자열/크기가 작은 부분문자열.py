def solution(t, p):
    answer = 0
    
    for i in range(len(t) - len(p) + 1):
        tmp = int(t[i : i + len(p)])
        print(tmp)
        if tmp <= int(p):
            answer += 1
        
    return answer