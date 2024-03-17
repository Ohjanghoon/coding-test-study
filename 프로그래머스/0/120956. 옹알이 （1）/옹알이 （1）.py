# 발음: aya, ye, woo, ma

def solution(babbling):
    answer = 0
    sounds = ["aya", "ye", "woo", "ma"]
    speak_set = {}
    
    for b in babbling:
        if b in sounds:
            answer += 1
        else:
            tmp = ''
            speakable = True
            for i in b:
                tmp += i
                if tmp in sounds:
                    tmp = ''
                    speakable = True
                else:
                    speakable = False
                
            if speakable:
                answer += 1
                
        
        
    
    return answer