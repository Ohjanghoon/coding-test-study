# 아이디: 알파벳 소문자, 숫자, -, _, .
# 단, 마침표는 처음, 끝, 연속 사용x
def solution(new_id):
    answer = ''
    special_character = ['-', '_', '.']
    
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    for i in new_id:
        if not i.isalnum() and i not in special_character:
            continue
        answer += i
    
    # 3단계
    while ".." in answer:
        answer = answer.replace('..', '.')
    
    # 4단계
    if len(answer) > 0 and answer[0] == '.':
        answer = answer[1:]
            
    if len(answer) > 0 and answer[-1] == '.':
        answer = answer[:-1]
    
    # 5단계
    if len(answer) == 0: answer = 'a'
    
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    
    # 7단계
    if len(answer) <= 2:
        for _ in range(3 - len(answer)):
            answer += answer[-1]
        
    return answer