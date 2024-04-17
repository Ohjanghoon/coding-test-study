# 10일 동안 회원 자격 부여
# 할인 제품 하루에 1개 구매 가능

def solution(want, number, discount):
    answer = 0
    
    list_all_want = []

    for i in range(len(want)):
        for j in range(number[i]):
            list_all_want.append(want[i])
    list_all_want.sort()

    for i in range(len(discount) - 9):
        list_10 = discount[i: i+10]
        list_10.sort()
        if list_all_want == list_10:
            answer += 1
    
#     dis_day = []
#     flag = False
    
#     for i in range(len(want)):
#         if want[i] not in discount:
#             return 0
#         else:
#             tmp = discount[discount.index(want[i]):]
#             for w, n in zip(want, number):
#                 if n == tmp.count(w):
#                     print(tmp)
#                     flag = True
#                 else:
#                     flag = False
#                     break
                    
#             if flag == True:
#                 answer += 1

    return answer