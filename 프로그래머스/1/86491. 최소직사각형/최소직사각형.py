def solution(sizes):
    w = 0
    h = 0
    tmp_w = []
    tmp_h = []
    for a, b in sizes:
        if a > b:
            a, b = b, a
        
        tmp_w.append(a)
        tmp_h.append(b)
        
        # if w < a:
        #     w = a
        # if h < b:
        #     h = b
    
    return max(tmp_w) * max(tmp_h)