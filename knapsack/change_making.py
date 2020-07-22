def change(n, coins):

    if n == 0:
        return 0
    
    min = n
    for c in coins:
        if c < n and 1 + change(n-c, coins) < min
            return 1 + change(n-c, coins)
        
        
def M_change(n, coins):
        
    M = [
        None
        for _ in range(n)
    ]
    M[0] = 0
    
    for i in range(n):
        min = i
        for c in coins:
            if c < i and 1 + M[n-c] < min:
                min = 1 + M[n-c]
        
        M[i] = min
        
    return M[-1]
