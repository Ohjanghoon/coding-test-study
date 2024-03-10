def solution(n):
    sample_str = '수박'
    answer = ''
    
    for i in range(n):
        answer += sample_str[i % 2]
            
    return answer