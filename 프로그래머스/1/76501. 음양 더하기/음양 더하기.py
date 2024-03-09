def solution(absolutes, signs):
    answer = 0
    
    # enumerate(): 인덱스와 값을 동시에 열거
    for idx, val in enumerate(absolutes):
        # signs[idx]가 true일 경우 양수, false일 경우 음수 누적합
        answer += val if signs[idx] else -val
            
        
    return answer