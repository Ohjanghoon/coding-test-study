def solution(s):
    answer = []
    word_dict = {}
    
    for idx, alphabet in enumerate(s):
        if alphabet not in word_dict.keys():
            word_dict[alphabet] = idx
            answer.append(-1)
        else:
            answer.append(idx - word_dict[alphabet])
            word_dict[alphabet] = idx
        
            
    return answer