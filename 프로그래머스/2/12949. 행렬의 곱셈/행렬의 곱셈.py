# [[1,4],   [[3,3]
# [3,2],  *  [3,3]]
# [4,1]]

# [2,3,2]   [5,4,3]
# [4,2,4] * [2,4,1]
# [3,1,4]   [3,1,1]

def solution(arr1, arr2):
    answer = []
    
    # 2차 시도
    for i in range(len(arr1)) :
        list = []
        for j in range(len(arr2[0])) :
            a = 0
            for k in range(len(arr1[0])):
                a += arr1[i][k] * arr2[k][j]
                
            list.append(a)
        answer.append(list)
                
    return answer
        
    
#     # 1차 시도(numpy 활용)
#     arr1 = np.array(arr1)
#     arr2 = np.array(arr2)
    
#     return np.dot(arr1, arr2).tolist()