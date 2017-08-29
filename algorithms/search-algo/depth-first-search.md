# Depth-First Search for G = (V, E)

DFS is a recursive algorithm using the idea of backtracking. It takes in worst-case time `O(|V|+|E|)` for explicit graphs. DFS can detect if an undirected graph contains a cycle.

Pseudocode:

```
unmark all nodes;
init
foreach s ∈ V do
    if s is not marked then
        mark s // make s a root and grow
        root(s)
        DFS(s, s)

Procedure DFS(u, v : NodeId)    // explore v coming from u
    foreach (v, w) ∈ E do
        if w is marked then
            traverseNonTreeEdge(v, w)
        else
            traverseTreeEdge(v, w)
            mark w
            DFS(v, w)
    backtrack(u, v) // return from v along the incoming edge
```

```
Procedure init()
    parent = <⊥,...,⊥> : NodeArray of NodeId

Procedure root(s : NodeId)
    parent[s] := s

Procedure traverseTreeEdge(v, w : NodeId)
    parent[w] := v

Procedure traverseNonTreeEdge(v, w : NodeId)
    print "The graph contains a cycle!"
```
