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
    
    n = len(values)
    M = [[
        0
        for _ in range(size)
    ]   for _ in range(n)
    ]
    
    for i in range(n):
        for s in range(size):
            
            if weights[i] > s:
                M[i][s] = M[i-1][s]
                
            else:
                M[i][s] = max(
                    M[i-1][s], 
                    M[i-1][s - weights[i]] + values[i]
                )
    
    return M[-1][-1]
