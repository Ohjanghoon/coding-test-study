def solution(s):
    
    answer = []
    words = s.split(" ")
    
    # 1번째 시도
    for word in words:
        temp_text = ''
        for i in range(len(word)):
            if i % 2 == 0:
                temp_text += word[i].upper()
            else:
                temp_text += word[i].lower()
        
        answer.append(temp_text)
        
    return " ".join(answer)
