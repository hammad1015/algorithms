def floyd_warshall(verticies, edges, weights):
    
    v   = len(verticies)                    # number of verticies in graph
    e   = len(edges)                        # number of edges in graph
    inf = max(weights) * e                  # virtual infinity
    
    dist = [[                               # initializing distance matrix
        inf                                 
        for _ in range(n)
    ]   for _ in range(n)
    ]
    
    for i in range(n):                      # distance from each vertex to itself equals 0
        dist[i][i] = 0
        
    for i in range(e):                      # distance between two verticies equals 
        v1 = verticies.index(edges[i][0])   # the weight of the edge between them, if any
        v2 = verticies.index(edges[i][1])
        
        dist[v1][v2] = weights[i]
    
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                dist[i][k] = min(           # minimum distance between two verticies is covered either by
                    dist[i][j],             # moving to the second vertex directly or
                    dist[i][k] + dist[k][j] # moving to an intermediate vertex before moving to the second vertex
                )
                
    return dist



def bellman_ford(vertex, verticies, edges, weights):
    
    v   = len(verticies)
    e   = len(edges)
    inf = max(weights) * e
    
    vertex = verticies.index(vertex)
    
    dist = [
        inf
        for _ in range(v)
    ]
    for i in range(e):
        v1 = verticies.index(edges[i][0])
        v2 = verticies.index(edges[i][1])
        
        if v1 == vertex: dist[v2] = weight[i]
        if v2 == vertex: dist[vi] = weight[i]
            
    for i in range(e):
        v1 = verticies.index(edges[i][0])
        v2 = verticies.index(edges[i][1])
        
        dist[v2] = min(
            dist[v2],
            dist[v1] + weight[i]
        )
        
    return dist
