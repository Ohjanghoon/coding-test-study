# n: 전체 학생 수
# lost: 도난당한 학생들 번호
# reserve: 여벌옷 가져온 학생들 번호
def solution(n, lost, reserve):
    answer = 0
    
    keep = n - len(lost)
    lost.sort()
    reserve.sort()
    
    save = []
    save_count = 0
    for re in reserve:
        tmp = []
        if re in lost:
            save_count += 1
            lost.pop(lost.index(re))
            continue
        
        if re - 1 > 0:
            tmp.append(re - 1)
        if re + 1 <= n:
            tmp.append(re + 1)
        save.append(tmp)
    
    for lo in lost:
        print(save)
        for idx, sa in enumerate(save):
            if lo in sa:
                save_count += 1
                save.pop(idx)
                continue
    
    return keep + save_count