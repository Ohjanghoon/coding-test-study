# data: [코드번호(code), 제조일(date), 최대 수량(max), 현재 수량(remain)]
# ext: 데이터 추출 기준
# val_ext: 추출 기준 값
# sort_by: 정보 정렬 기준 str
def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    
    data_idx = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    ext_idx = data_idx[ext]
    tmp = []
    for info in data:
        if info[ext_idx] < val_ext:
            tmp.append(info)
            
    answer = sorted(tmp, key = lambda x:x[data_idx[sort_by]])
    
    return answer