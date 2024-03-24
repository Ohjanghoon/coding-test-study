# 매우 동의, 매우 비동의: 3점
# 동의, 비동의: 2점
# 약간 동의, 약간 비동의: 1점
# 모르겠음: 0점
# 하나의 지표에서 동일한 점수일 경우, 사전순으로 빠른 성격유형으로 판단

def solution(survey, choices):
    answer = ''
    characters = ["R", "T", "C", "F", "J", "M", "A", "N"]
    scores = [0, 0, 0, 0, 0, 0, 0, 0]
    
    for idx, choice in enumerate(choices):
        if choice < 4:
            key = survey[idx][0]
            score = 4 - choice
        elif choice > 4:
            key = survey[idx][1]
            score = choice - 4
        else:
            continue
        
        scores[characters.index(key)] += score
    

    for idx in range(0, len(characters), 2):
        if scores[idx] > scores[idx + 1]:
            answer += characters[idx]
        elif scores[idx] < scores[idx + 1]:
            answer += characters[idx + 1]
        else:
            answer += characters[idx]
        
    return answer