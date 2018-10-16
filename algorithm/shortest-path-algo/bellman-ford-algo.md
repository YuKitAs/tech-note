# Bellman-Ford Algorithm

Unlike Dijkstra's algorithm, Bellman-Ford algorithm can be used on graphs with negative edge weights, as long as the graph contains no negative cycle reachable from the starting node.

Pseudocode:

```
Function BF(s : NodeId, (V, E) : Graph): Array of distances
    d := <∞,...,∞> : Array of distances
    d[s] := 0
    for i = 1 to n - 1 do
        forall e = (u, v) ∈ E do
            if d[v] > d[u] + c[e] then
                d[v] := d[u] + c[e]
    forall e = (u, v) ∈ E do
        if d[v] > d[u] + c[e] then
            stop    // a negative cycle detected
    return d
```
