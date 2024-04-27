# bridge_length: 다리에 올라갈 수 있는 트럭 수(다리 길이)
# weight: 다리가 견딜 수 있는 무게
# truck_weights: 트럭 별 무게
# return - 최소 몇 초가 걸리는지
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    bridge = deque([0 for _ in range(bridge_length)])
    truck_weights = deque(truck_weights)
    
    curr_weight = 0
    # 모든 트럭이 나갈 때 까지
    while len(truck_weights) > 0:
        answer += 1
        curr_weight -= bridge.pop()
        
        if curr_weight + truck_weights[0] <= weight:
            curr_weight += truck_weights[0]
            bridge.appendleft(truck_weights.popleft())
        else:
            bridge.appendleft(0)
        
    
    return answer + bridge_length