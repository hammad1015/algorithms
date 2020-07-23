def floyd_warshall(verticies, edges, weights):
    
    v = len(graph)
    e = len(edges)
    dist = [[
        None 
        for _ in range(n)]
        for _ in range(n)
    ]
    for i in range(n):
        dist[i][i] = 0
        
    for i in range(e):
        v1 = verticies.index(edges[i][0])
        v2 = verticies.index(edges[i][1])
        
        dist[v1][v2] = weights[i]
        
    for i in range(n):
        for j in range(n):
            for k in range(n):
                dist[i][k] = min(
                    dist[i][j],
                    dist[i][k] + dist[k][j]
                )
                
    return dist
        
