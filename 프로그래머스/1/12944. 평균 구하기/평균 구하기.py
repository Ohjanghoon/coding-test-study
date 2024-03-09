def solution(arr):
    answer = 0
    for val in arr:
        answer += val
    answer /= len(arr)
    return answer