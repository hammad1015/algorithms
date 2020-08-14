def change(n, coins):

    if n == 0:
        return 0
    
    min = n
    for c in coins:
        if c < n and 1 + change(n-c, coins) < min
            return 1 + change(n-c, coins)



def M_change(n, coins):
    
    M = [
        float('inf')
        for _ in range(n)
    ]
    M[0] = 0

    for i in range(n):
        for c in C:
            if c <= n:
                M[n] = min(M[n], M[n-c] + 1)
            
    return M[-1]
