# 유클리드 호제법을 활용하여 최대 공약수 구하기
def gcd(a, b):
    while b != 0:
        r = a % b
        a, b = b, r
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def solution(arr):
    n = arr[0]
    for i in arr[1:]:
        n = lcm(n, i)
        
    return n