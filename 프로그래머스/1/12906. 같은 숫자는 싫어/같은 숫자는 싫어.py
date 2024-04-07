def solution(arr):
    answer = []
    
    # 2차 시도(스택 활용)
    for num in arr:
        answer.append(num)
        if len(answer) >= 2:
            if answer[-2] == answer[-1]:
                answer.pop(-1)
    
    # 1차 시도
    # for idx in range(len(arr)):
    #     if idx + 1 < len(arr) and arr[idx] == arr[idx + 1]:
    #         continue
    #     else:
    #         answer.append(arr[idx])
        
    return answer