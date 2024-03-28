def solution(s):
    tmp = [int(num) for num in s.split(' ')]
    return str(min(tmp)) + " " + str(max(tmp))