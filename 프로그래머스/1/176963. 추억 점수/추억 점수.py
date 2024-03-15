# name: 그리워하는 사람의 이름 배열
# yearing: 사람별 그리움 점수 배열
# photo: 사진에 찍힌 인물의 이름을 담은 이차원 배열

def solution(name, yearning, photo):
    answer = []
    
    for people in photo:
        tmp = 0
        for p in people:
            if p in name:
                idx = name.index(p)
                tmp += yearning[idx]
        answer.append(tmp)
    return answer

