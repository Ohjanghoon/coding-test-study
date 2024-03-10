def solution(arr1, arr2):
    answer = []
    
    for idx_1, row in enumerate(arr1):
        tmp = []
        for idx_2, val in enumerate(row):
            tmp.append(val + arr2[idx_1][idx_2])
        answer.append(tmp)
        
            
    return answer