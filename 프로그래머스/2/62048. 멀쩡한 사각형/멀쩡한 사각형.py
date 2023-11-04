import math
def solution(w,h):
    g = math.gcd(w,h)
    return w*h-g*((w/g)+(h/g)-1)