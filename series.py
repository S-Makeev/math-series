
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)
#https://www.geeksforgeeks.org/lucas-numbers/# - used this as a reference 
def sum_series(n, n2, n3):
    if n2 == 0 and n3 == 1:
        return fibonacci(n)
    elif n2 == 2 and n3 == 1:
        return lucas(n)
    else:
        return sum_series(n-1) + sum_series(n-2)
    