def knapsack(i, size):
    
    if size == 0 or i == 0:
        return 0
    
    if weights[i] > size:
        return knapsack(i-1, size)
    
    return max(
        knapsack(i-1, size),
        knapsack(i-1, size - weights[i]) + values[i]
    )

    
def M_knapsack(weights, values, size):
    
    n = len(weights)
    M = [[
        None 
        for _ in range(size)]
        for _ in range(n)
    ]
    
    for i in range(size): M[0][i] = 0
    for i in range(n)   : M[i][0] = 0
    
    for i in range(n):
        for j in range(size):
            if M[i][j] == None:
                M[i][j] = max(
                    M[i-1][j], 
                    M[i-1][size - weights[i]] + values[i]
                )
    
    return M[i][size]
