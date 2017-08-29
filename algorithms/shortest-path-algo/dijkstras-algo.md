# Dijkstra's Algorithm

Pseudocode:

```
init d, parent
all nodes are non-scanned
while ∃ non-scanned node u with d[u] < ∞
    u := non-scanned node v with minimal d[v]
    relax all edges (u, v) out of u
    u is scanned now
```

```
Procedure relax()
    if d[u] + c(u, v) < d[v] then
        d[v] := d[u] + c(u, v)
        parent[v] := u
```

With binary heap the algorithm requires time `O((|E|+|V|)log|V|)` in worst-case, and the Fibonacci heap improves it to `O(|E|+|V|log|V|)`, where `|E|` is the number of edges and `|V|` the number of nodes.
