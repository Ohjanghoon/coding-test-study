# people: 사람들의 몸무게를 담은 배열
# limit: 무게 제한
# 무게 범위: 40 <= kg <= 240
def solution(people, limit):
    answer = 0
    boat = []
    
    # 3차 시도(start, end 인덱스로 접근)
    people.sort()
    i = 0
    j = len(people) - 1
    while i <= j:
        if i == j:
            boat.append([people[i]])
            break
        
        if people[i] + people[j] <= limit:
            boat.append([people[i], people[j]])
            i += 1
            j -= 1
        else:
            boat.append([people[j]])
            j -= 1
    
    return len(boat)
    
    
    # 2차 시도(효율성 1번 시간 초과)
#     people.sort()
#     while len(people) > 0:
#         if len(people) > 1:
#             min_w = people[0]
#             max_w = people[-1]
        
#             if min_w + max_w <= limit:
#                 boat += 1
#                 people.pop(0)
#                 people.pop(-1)
#             else:
#                 boat += 1
#                 people.pop(-1)
                
#         elif len(people) == 1:
#             boat += 1
#             people.pop()
#             break
    
    
    # 1차 시도 
    # 무게제한에 의해 혼자만 타야되는 사람 미리 태우기
#     for p in people:
#         if limit - p < 40:
#             boat.append(p)
#         else:
#             ridable.append(p)
    
#     ridable.sort()
#     while len(ridable) > 0:
#         if len(ridable) > 1:
#             min_w = ridable[0]
#             max_w = ridable[-1]
        
#             if min_w + max_w <= limit:
#                 boat.append([min_w, max_w])
#                 ridable.pop(0)
#                 ridable.pop(-1)
#             else:
#                 boat.append([max_w])
#                 ridable.pop(-1)
                
                
#         elif len(ridable) == 1:
#             boat.append(ridable[0])
#             people.pop()
#             break
#         else:
#             break
        
    # return boat