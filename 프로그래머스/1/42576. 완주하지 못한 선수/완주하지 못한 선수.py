# participant: 참여한 선수 배열
# completion: 완주한 선수 이름
# return - 완주 못한 선수 이름
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    for idx, par in enumerate(participant):
        if len(completion) <= idx:
            return participant[-1]
            
        if par != completion[idx]:
            answer = participant[idx]
            break
            
    return answer
    