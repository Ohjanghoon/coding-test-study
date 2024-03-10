def solution(arr):
    answer = []
    
    for idx in range(len(arr)):
        if idx + 1 < len(arr) and arr[idx] == arr[idx + 1]:
            continue
        else:
            answer.append(arr[idx])
        
    return answer