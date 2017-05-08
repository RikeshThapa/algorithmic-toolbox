# Uses python3
import sys

def get_change(m):
    change = 0
    val =0
    while val<m:
        l = m-val
        if l>=10:
            val+=10
            change +=1
        elif l>=5:
            val+=5
            change+=1
        elif l>=1:
            val+=1
            change+=1
    return change


m = int(input())
print(get_change(m))
