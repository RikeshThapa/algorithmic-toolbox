# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd_euclid(a, b):
    small = min(a,b)
    big = max(a,b)
    current_gcd = small
    mod = big%small
    while mod!=0:        
        new_gcd = mod
        mod = current_gcd%mod
        current_gcd = new_gcd
    return current_gcd

def lcm_rt(a, b):
    gcd = gcd_euclid(a,b)
    a1 = int(a/gcd)
    b1 = int(b/gcd)
    lcm = gcd*a1*b1
    return lcm


input = input()
a, b = map(int, input.split())
print(lcm_rt(a, b))

