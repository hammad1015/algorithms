def factorial(n):
    
    if n == 0:
        return 1
    
    return n * factorial(n-1)

def m_factorial(n):
    
    r = 1
    for i in range(1, n+1):
        r = r * i
        
    return r
