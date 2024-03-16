# keymap: 1번 키부터 차례로 할당된 문자열 배열
# targets: 입력하려는 문자열 배열
# return - targets의 문자열을 입력하기 위한 최소 횟수(작성 불가 -1)

def solution(keymap, targets):
    answer = []
    
    # key맵에 있는 문자열들의 최소 클릭 횟수
    alphabet_count = {}
    for key in keymap:
        for idx, alphabet in enumerate(key):
            if alphabet in alphabet_count.keys():
                if alphabet_count[alphabet] > idx + 1:
                    alphabet_count[alphabet] = idx + 1    
            else:
                alphabet_count[alphabet] = idx + 1
    print("alphabet_count ===> ", alphabet_count)
    
    # 입력하려는 문자열의 최소 횟수 찾기
    for target in targets:
        tmp = 0
        for alphabet in target:
            # keymap에 없을 경우
            if alphabet not in alphabet_count.keys():
                tmp = -1
                break
            else:
                tmp += alphabet_count[alphabet]
        
        answer.append(tmp)
            
    
    return answer