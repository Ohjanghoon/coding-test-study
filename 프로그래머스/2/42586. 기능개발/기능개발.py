# 진도가 100% 일 때, 서비스에 반영 가능.
# 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포.
# progresses: 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열
# speeds: 작업의 개발 속도가 적힌 정수 배열
# return - 각 배포마다 몇 개의 기능이 배포되는지
from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    
    period = deque([])
    for i in range(len(progresses)):
        period.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    cnt = 1
    release_date = period.popleft()
    while len(period) > 0:
        tmp = period.popleft()
        if release_date >= tmp:
            cnt += 1
        else:
            answer.append(cnt)
            release_date = tmp
            cnt = 1
        
        if len(period) == 0:
            answer.append(cnt)
    
    return answer