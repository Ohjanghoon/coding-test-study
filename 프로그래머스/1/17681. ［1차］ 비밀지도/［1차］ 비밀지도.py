# n: 정사각형 한 변의 길이
# 1: 벽, 0: 공백

def solution(n, arr1, arr2):
    answer = []
    
    # bin(int) 함수를 이용하여 2진수 변환 -> 문자열 타입으로 반환
    # zfill을 통해서 문자열 자릿수 맞추기 => 빈 자리는 0으로 채움
    for idx, i in enumerate(arr1):
        arr1[idx] = bin(i)[2:].zfill(n)
        
    for idx, j in enumerate(arr2):
        arr2[idx] = bin(j)[2:].zfill(n)
    
    for x in range(n):
        tmp = ''
        for y in range(n):
            if arr1[x][y] == '1' or arr2[x][y] == '1':
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)
            
        
    
    return answer