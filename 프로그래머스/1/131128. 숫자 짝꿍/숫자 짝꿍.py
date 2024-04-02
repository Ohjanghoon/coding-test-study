def solution(X, Y):
    answer = ''
    
    # 1번째 시도(11 ~ 15 시간초과)
#     sort_x = sorted(X, reverse=True)
#     sort_y = sorted(Y, reverse=True)
    
#     tmp = []
#     for x in sort_x:
#         if x in sort_y:
#             tmp.append(x)
#             sort_y = sort_y[sort_y.index(x) + 1:]
#             answer += x
    
    tmp = []
    for i in range(9, -1, -1):
        answer += str(i) * min(X.count(str(i)), Y.count(str(i)))    
        
    if answer == '':
        return "-1"
    elif answer[0] == "0":
        return "0"
    
    return answer