def solution(arr):
    answer = []
    
    if len(arr) == 1:
        answer = [-1]
    else:
        # 가장 작은 수가 있는 원소의 인덱스를 찾아 리스트에서 삭제
        del arr[arr.index(min(arr))]
        answer = arr
    return answer