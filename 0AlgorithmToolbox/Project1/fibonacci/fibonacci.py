# Uses python3
#This is an extremely naieve solution, takes O(n^2) time to complete, because of
# recursive startegy
'''def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

n = int(input())
print(calc_fib(n))
'''

def calc_fib(n):
    finarr = []
    i =0
    while i<=n:
        if i==0:
            finarr.append(0)
        elif i==1:
            finarr.append(1)
        else:
            newVal = finarr[i-1]+finarr[i-2]
            finarr.append(newVal)
        i +=1
    return finarr[n]

n= int(input())
print(calc_fib(n))
    



