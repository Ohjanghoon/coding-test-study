# citations: 논문 인용 횟수 배열
def solution(citations):
    citations.sort();
    
    tmp = []
    for i in range(len(citations)):
        length = len(citations[i:])
        if length < citations[i]:
            tmp.append(length)
        else:
            tmp.append(citations[i])
    
    return max(tmp)