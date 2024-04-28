# return - 어떤 번호가 다른 번호의 접두어인 경우 false, 그렇지 않으면 true

def solution(phone_book):
    
    # 2차 시도(정렬 수정)
    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
        
    return True
    
    
    # 1차 시도(효율성 3,4 시간 초과)
    # phone_book.sort(key=len)
    
#     for i in range(len(phone_book) - 1):
#         for j in range(i + 1, len(phone_book)):
#             if phone_book[j].startswith(phone_book[i]):
#                 return False
    
#     return True