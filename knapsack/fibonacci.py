def fibonacci(n):
    
    if n == 0 or n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

def M_fibonacci(n):
    
    a = 0
    b = 1
    for _ in range(n):
        c = a + b
        a = b
        b = c
        
    return b
