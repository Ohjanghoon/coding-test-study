import numpy as np

def solution(arr1, arr2):
    
    #1. 파이썬 일반적인 풀이 사용
#     answer = []
    
#     for idx_1, row in enumerate(arr1):
#         tmp = []
#         for idx_2, val in enumerate(row):
#             tmp.append(val + arr2[idx_1][idx_2])
#         answer.append(tmp)
    
    #2. numpy 활용
    answer = [[]]
    
    # tolist()를 활용하여 list 타입으로 변환
    answer = (np.array(arr1) + np.array(arr2)).tolist()
            
    return answer