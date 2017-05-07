# Uses python3

'''
def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        print(d)
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd'''

#new mods should give O(n)
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

input = input()
a, b = map(int, input.split())
print(gcd_euclid(a, b))
