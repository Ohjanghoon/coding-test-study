def solution(elements):
    answer = 0
    elements *= 2
    prog = set([])
    for i in range(1, len(elements) // 2 + 1):
        for j in range(len(elements) // 2):
            prog.add(sum(elements[j : j + i]))

    return len(prog)