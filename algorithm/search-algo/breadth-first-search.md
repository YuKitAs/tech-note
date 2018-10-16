# Breadth-First Search for G = (V, E)

BFS starts at the tree root and explores the neighbor nodes first before moving to the next level neighbors. It takes in worst-case time `O(|V|+|E|)`.

Pseudocode:

```
Function bfs(s : NodeId):
    Q := <s>    // current level
    while Q ≠ <> do
        explore nodes in Q
        save nodes of the next level in Q'
        Q := Q'
```

```
Procedure doBFS(G)  
/* for disconnected, undirected graphs */
    foreach v ∈ V do
        if v is not marked then
            bfs(v)

Procedure doBFS(G)
/* for disconnected, directed graphs */
    b: Array of {0, 1}
    foreach v ∈ V do
        b[v] := 1
    foreach (u, v) ∈ E do
        b[v] := 0
    /* all the roots are now marked */
    foreach v ∈ V and b[v] = 1 do
        bfs(v)
```
