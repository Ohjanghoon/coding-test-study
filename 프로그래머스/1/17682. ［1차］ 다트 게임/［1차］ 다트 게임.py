# 다트 3번 던져 그 점수 합계
# 얻을 수 있는 점수 0~10점
# S: 1제곱, D: 2제곱, T: 3제곱
# *: (해당 점수 + 바로 전 점수) * 2
# #: 해당 점수 * -1

def solution(dartResult):
    answer = 0
    dart_dict = {}
    
    scores = [0 for _ in range(3)]
    idx = -1
    tmp_num = ""
    tmp_score = 0
    for i, re in enumerate(dartResult):
        if re.isdigit():
            tmp_num += re
            if dartResult[i + 1].isdigit():
                continue
            idx += 1
            num = int(tmp_num)
            tmp_score = 0
        
        if re == 'S':
            tmp_score = num ** 1
        elif re == 'D':
            tmp_score = num ** 2
        elif re == 'T':
            tmp_score = num ** 3
        elif re == '*':
            tmp_score *= 2
            scores[idx - 1] *= 2
        elif re == '#':
            tmp_score *= -1
        scores[idx] = tmp_score
        
        tmp_num = ""
    
    return sum(scores)