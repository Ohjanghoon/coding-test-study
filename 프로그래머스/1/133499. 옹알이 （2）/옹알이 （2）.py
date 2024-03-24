def solution(babbling):
    answer = 0
    
    speak_word = ["aya", "ye", "woo", "ma"]
    
    for b in babbling:
        if b in speak_word:
            answer += 1
        else:
            tmp = ''
            prev = ''
            speakable = False
            for a in b:
                tmp += a
                if tmp in speak_word and prev != tmp:
                    prev = tmp
                    tmp = ''
                    speakable = True
                else:
                    speakable = False
            
            if speakable:
                answer += 1
                
    
    return answer