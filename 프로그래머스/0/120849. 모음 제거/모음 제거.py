def solution(my_string):
    answer = ''
    vowel = ["a", "e", "i", "o", "u"]
    
    for ms in my_string:
        if ms not in vowel:
            answer += ms
    return answer