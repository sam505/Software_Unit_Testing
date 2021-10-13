def addEdge(adj, v, w):
    adj[v].append(w)

    # Note: the graph is undirected
    adj[w].append(v)
    return adj


def greedyColoring(adj, V):
    result = [-1] * V

    # Assign the first color to first vertex
    result[0] = 0

    available = [False] * V

    for u in range(1, V):
        # Process all adjacent vertices and
        # flag their colors as unavailable
        for i in adj[u]:
            if result[i] != -1:
                available[result[i]] = True
        # Find the first available color

        cr = 0
        while cr < V:
            if not available[cr]:
                break
            cr += 1
        # Assign found color
        result[u] = cr

        # Resetting the values back to False for next iteration
        for i in adj[u]:
            if result[i] != -1:
                available[result[i]] = False

        # Print the result
        for u in range(V):
            print("Vertex", u, "---> Color", result[u])


def main():
    g1 = [[] for i in range(5)]
    g1 = addEdge(g1, 0, 1)
    g1 = addEdge(g1, 0, 2)
    g1 = addEdge(g1, 1, 2)
    g1 = addEdge(g1, 1, 3)

    g1 = addEdge(g1, 2, 3)
    g1 = addEdge(g1, 3, 4)
    print("Coloring of graph 1 ")
    greedyColoring(g1, 5)

    g2 = [[] for i in range(5)]
    g2 = addEdge(g2, 0, 1)
    g2 = addEdge(g2, 0, 2)
    g2 = addEdge(g2, 1, 2)
    g2 = addEdge(g2, 1, 4)

    g2 = addEdge(g2, 2, 4)
    g2 = addEdge(g2, 4, 3)
    print("\nColoring of graph 2")
    greedyColoring(g2, 5)


if __name__ == "__main__":
    main()
