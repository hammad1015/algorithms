""" 
Node : any_hashable_obj
Graph: dict[Node, dict[Node, int]] 
"""

def floyd_warshall(graph: Graph) -> Graph:
    
    """ takes in a graph and returns a fully connected copy of it,
        where the weight of edge between two nodes equals the minimum 
        distance between the corresponding nodes of the orignal graph
    """
    
    inf = float('inf')                              # virtual infinity
    
    dist = { n1:{ n2:                               # initializing distance graph
        inf
        for n1 in graph
    }   for n2 in graph
    }
    
    for n in graph:                                 # distance from each node to itself equals 0
        dist[n][n] = 0
        
    for n1 in graph:                                # distance between two nodes equals weight of edge between them 
        for n2 in graph[n1]:
            dist[n1][n2] = graph[n1][n2]
    
    
    for n1 in graph:
        for n2 in graph:
            for n3 in graph:
                dist[n1][n2] = min(                 # minimum distance between two verticies is covered either by
                    dist[n1][n2],                   # moving to the second vertex directly or
                    dist[n1][n3] + dist[n3][n2]     # moving to an intermediate vertex, then moving to the second vertex
                )
                
    return dist



def bellman_ford(vertex: Node, graph: Graph) -> dict[Node, int]:
    
    """ takes in a node "vertex" and a graph, and returns a map
        of graph's nodes and their minimum distance to "vertex"
    """
    
    inf = float('inf')                      # virtual infinity
    
    dist = {                                # initializing distance map
        n: inf
        for n in graph
    }
    
    for n in graph[vertex]:
        dist[n] = graph[vertex][n]          # distance from "vertex" to it's neighbours equals the weight of edge between them
        
    for n1 in graph:
        for n2 in graph[n1]:
            dist[n2] = min(                 # minimum distance between "vertex" and any other node is either 
                dist[n2],                   # the currently agreed minimum distance to the node or
                dist[n1] + graph[n1][n2]    # the distance to its neighbour + weight of edge between it and the neighbour
            )
        
    return dist
