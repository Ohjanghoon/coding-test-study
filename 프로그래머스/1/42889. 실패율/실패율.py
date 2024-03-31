# 실패율: 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# N: 전체 스테이지 개수
# stages: 현재 멈춰있는 스테이지의 번호 배열
# return - 실패율이 높은 스테이지부터 내림차순 배열(실패율이 같다면 작은 번호가 앞으로)

def solution(N, stages):
    tmp = {}
    for n in range(1, N + 1):
        arrived_stage = [s for s in stages if n <= s]
        if len(arrived_stage) > 0:
            tmp[n] = arrived_stage.count(n) / len(arrived_stage)
        else:
            tmp[n] = 0
    
    tmp = sorted(tmp.items(), key = lambda x: (-x[1], x[0]))
    answer = [item[0] for item in tmp]
        
    return answer