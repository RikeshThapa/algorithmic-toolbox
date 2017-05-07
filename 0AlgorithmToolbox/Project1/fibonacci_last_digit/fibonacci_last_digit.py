# Uses python3

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    i=0

    while i<(n-1):
        #Here is the simple fix to make the program, 
        previous, current = current, (previous + current)%10
        i+=1
    return current % 10

n = int(input())
print(get_fibonacci_last_digit_naive(n))
