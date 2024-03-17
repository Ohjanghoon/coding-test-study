# k: 사과의 최고 점수
# m: 한 상자에 사과 개수
# return - 가능한 많은 사과를 팔았을 때, 얻을 수 있는 최대 이익 계산(이익 발생 x => 0)

def solution(k, m, score):
    answer = 0
    boxes = []
    
    # 최고 점수순으로 내림차순 정렬
    score.sort(reverse = True)
    
    # 박스 포장하기(남는 사과는 버려짐)
    for i in range(len(score) // m):
        boxes.append(score[i*m : (i+1) * m])
    
    for box in boxes:
        # 최저 사과 점수 * 사과 개수
        answer += min(box) * m
    
    
    return answer