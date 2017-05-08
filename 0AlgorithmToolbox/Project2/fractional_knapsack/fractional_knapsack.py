# Uses python3
from __future__ import division
import sys
import time


def get_optimal_value(capacity, weights, values):
    value = 0.
    currentWeight = 0.
    fractionalValues = [a/b for a, b in zip(values, weights)]
    unsorted = fractionalValues
    fractionalValues = sorted(fractionalValues, reverse=True)
    i=0
    curmaxval = fractionalValues[i]
    index = unsorted.index(curmaxval)
    while currentWeight<capacity and i<len(weights):
        if weights[index] ==0:
            i += 1
            curmaxval = fractionalValues[i]
            index = unsorted.index(curmaxval)
        if ((capacity-currentWeight)>=weights[index]) and i!=(len(weights)-1):
            value+=curmaxval
            currentWeight += 1.
            weights[index] = weights[index]-1
        elif i==(len(weights)-1) and ((capacity-currentWeight)<weights[index]):
            value+= (capacity-currentWeight)*curmaxval
            currentWeight+=capacity-currentWeight
        elif i==(len(weights)-1) and ((capacity-currentWeight)>=weights[index]):
            value+= curmaxval*weights[index]
            currentWeight+=weights[index]
            weights[index]-=weights[index]
            i+=1        
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
