# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    lastdigitsum = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current)%10
        lastdigitsum = (lastdigitsum+ current)%10

    return lastdigitsum

def get_fibonacci_fast(n, m):
    #Making list of fib numbers; We do not even have to go to the end
    pisano = []
    i =0
    pisanoend = False
    if n==1:
        return 1
    while i<=n and pisanoend!=True:
        if i==0:
            previous = 0
            pisano.append(0)
        elif i==1:
            current  = 1
            pisano.append(1)
        else:
            previous, current = current, previous + current
            pisano.append(current%m)
            if(pisano[i]==1 and pisano[i-1]==0):
                pisanoend=True
                del pisano[(i-1):]
        i +=1
        
    pisanolen = len(pisano)
    location = n%pisanolen
    return pisano[location]

n = int(input())
print(fibonacci_sum_naive(n))
