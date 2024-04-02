def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)
    
    for idx, a in enumerate(A):
        answer += a * B[idx]
        
        

    return answer