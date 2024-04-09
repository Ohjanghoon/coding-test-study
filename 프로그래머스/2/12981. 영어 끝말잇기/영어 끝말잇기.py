# n: 끝말잇기하는 사람 수
# words: 영단어 배열

def solution(n, words):
    already = []
    
    num = 0
    turn = 0
    
    for idx, w in enumerate(words):
        if w not in already:
            already.append(w)
        else:
            num = idx % n + 1
            turn = idx // n + 1
            break
        
        if idx > 0 and words[idx - 1][-1] != words[idx][0]:
            num = idx % n + 1
            turn = idx // n + 1
            break
    

    return [num, turn]