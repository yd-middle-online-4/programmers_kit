#https://luv-n-interest.tistory.com/736

import math

def solution(w,h):
    cross = math.gcd(w,h)
    return w*h-(w+h-cross)