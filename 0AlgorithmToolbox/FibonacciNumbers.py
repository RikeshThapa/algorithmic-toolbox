#n is expected length of fibonacci list
def fibonacci(n, start=0):
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
        #If I only want to start at val "start"
        if (i>=start):
            print(finarr[i])
        i +=1
    return finarr

fibonacci(100)
            
    
