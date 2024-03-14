def solution(wallpaper):
    x = []
    y = []
    
    for row_idx, row in enumerate(wallpaper):
        if '#' in row:
            x.append(row_idx)
            y.append(row.index('#'))
            y.append(row.rindex('#'))
            
    
    lux, rdx = min(x), max(x) + 1
    luy, rdy = min(y), max(y) + 1
    
    return [lux, luy, rdx, rdy]




# 빈칸: . / 파일: #
# 왼쪽 클릭: S(lux, luy) -> 드래그: E(rdx, rdy)