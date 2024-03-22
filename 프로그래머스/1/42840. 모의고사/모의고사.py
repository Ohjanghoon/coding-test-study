def solution(answers):
    answer = []
    
    # supo = {
    #     "1": [1, 2, 3, 4, 5],
    #     "2": [2, 1, 2, 3, 2, 4, 2, 5],
    #     "3": [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    # } 
    
    supo = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    scores = [0, 0, 0]
    for i, num in enumerate(answers):
        if num == supo[0][i % len(supo[0])]:
            scores[0] += 1
        
        if num == supo[1][i % len(supo[1])]:
            scores[1] += 1
            
        if num == supo[2][i  % len(supo[2])]:
            scores[2] += 1
        
    
    for i in range(len(scores)):
        if scores[i] == max(scores):
            answer.append(i + 1)
        
        # 런타임 에러
        # for j in range(len(supo)):
        #     if num == supo[j][i]:
        #         score[j] += 1
    
    answer.sort()
    return answer