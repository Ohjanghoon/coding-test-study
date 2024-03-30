# 햄버거 정해진 순서: 아래서부터 빵(1) - 야채(2) - 고기(3) - 빵(1)

def solution(ingredient):
    answer = 0
    
    tmp = []
    for i in ingredient:
        tmp.append(i)
        if tmp[-4:] == [1, 2, 3, 1]:
            answer += 1
            for i in range(4):
                tmp.pop()
            
    # 1번째 시도(string으로 활용 => 3, 4, 5, 6, 9, 12 실패,,,)
#     ingredient = ''.join(str(i) for i in ingredient)
    
#     while True:
#         if '1231' not in ingredient:
#             break
#         if '1231' in ingredient:
#             answer += ingredient.count('1231')
#             ingredient = ingredient.replace('1231', '')
            
    return answer
    
    