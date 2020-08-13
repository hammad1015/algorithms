def knapsack(i, size):
    
    if size == 0 or i == 0:
        return 0
    
    if weights[i] > size:
        return knapsack(i-1, size)
    
    return max(
        knapsack(i-1, size),
        knapsack(i-1, size - weights[i]) + values[i]
    )

    
def M_knapsack(items: list[tuple[float, float]], size: int) -> float:
    
    M = [[
        0
        for _ in range(size)
    ]   for _ in range(n)
    ]
    
    for i, (v, w) in enumerate(items):  # index, value and weight of the item:
        for s in range(size):
            
            if w > s:                   # if weight of the current item is more than the knapsack size
                M[i][s] = M[i-1][s]     # then we dont take it 
                
            else:                       # if weight of the current item is less than the knapsack size
                M[i][s] = max(          # we take it, if taking it maximises our total value
                    M[i-1][s],
                    M[i-1][s - w] + v
                )
    
    return M[-1][-1]
