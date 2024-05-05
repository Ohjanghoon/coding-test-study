# n행 n열의 비어있는 2차원 배열 생성
'''
0: 1 / 1: 2 / 2: 3
3: 2 / 4: 2 / 5: 3
6: 3 / 7: 3 / 8: 3
123|223|333
divmod(0, 3) = 0, 0
divmod(1, 3) = 0, 1
divmod(2, 3) = 0, 2
divmod(3, 3) = 1, 0
divmod(4, 3) = 1, 1
divmod(5, 3) = 1, 2
divmod(6, 3) = 2, 0
divmod(7, 3) = 2, 1
divmod(8, 3) = 2, 2

'''


def solution(n, left, right):
    answer = []
    
    # 3차 시도
    for i in range(left, right + 1):
        answer.append(max(divmod(i, n)) + 1)
    
    return answer
    # 2차 시도(시간 초과)
#     for i in range(n ** 2):
#         answer.append(max(divmod(i, n)) + 1)

#         if len(answer) == right + 1:
#             return answer[left:]



    # 1차 시도(시간 초과)
#     arr = [[0 for _ in range(n)] for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if i == j:
#                 arr[i][j] = i + 1
#             elif i < j:
#                 arr[i][j] = j + 1
#             else:
#                 arr[i][j] = i + 1
    
#     answer = sum(arr, [])[left : right + 1]
#     return answer