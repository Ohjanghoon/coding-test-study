import numpy as np

def solution(arr1, arr2):
    
    # 1차 시도(numpy 활용)
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    
    return np.dot(arr1, arr2).tolist()