def solution(sizes):
    w = 0
    h = 0
    
    for size in sizes:
        size.sort()
        if w < size[0]:
            w = size[0]
        if h < size[1]:
            h = size[1]
    
    return w * h