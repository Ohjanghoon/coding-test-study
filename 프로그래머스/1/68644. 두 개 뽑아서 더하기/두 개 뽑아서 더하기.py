def solution(numbers):
    answer = []
    
    # 2번째 풀이
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    
    return sorted(list(set(answer)))
    
    # 1번째 풀이
#     for i in range(len(numbers) - 1):
#         for j in range(i + 1, len(numbers)):
#             tmp = numbers[i] + numbers[j]
            
#             if tmp not in answer:
#                 answer.append(tmp)
            
#     answer.sort()
    
#     return answer