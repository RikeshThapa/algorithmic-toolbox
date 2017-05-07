# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0

'''
for i in range(0, n):
    for j in range(i+1, n):
        if a[i]*a[j] > result:
            #No need for long cast in python3 because int has been unified to conprise of both int and long
            #result = long(a[i])*long(a[j])
            result = a[i]*a[j]
'''

#This run is even faster than the solution proposed in the solution
no1 = -1
no2 = -1
for i in range(0,n):
    if i == 0:
        no1 = a[i]
    elif i == 1:
        if no1 > a[i]:
            no2 = no1
            no1 = a[i]
        else:
            no2 = a[i]
    else:
        if a[i] > no1:
            if a[i] > no2:
                no1 = no2
                no2 = a[i]
            else:
                no1 = a[i]

result = no1*no2
print(result)
