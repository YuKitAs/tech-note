-- Quicksort in Haskell
-- Pivot: the 1st element of the list

qsort [] = []
qsort (p:ps) = (qsort [x | x <- ps, x <= p]) ++ p:(qsort [x | x <- ps, x > p])
