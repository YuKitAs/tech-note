-- Merge sort in Haskell

mergeSort :: [Int] -> [Int]
mergeSort [] = []
mergeSort [x] = [x]
mergeSort xs = let (a, b) = splitAt ((length xs) `div` 2) xs
               in merge (mergeSort a) (mergeSort b)
               where merge [] ys = ys
                     merge xs [] = xs
                     merge (x:xs) (y:ys) = if x <= y then x:(merge xs (y:ys)) else y:(merge ys (x:xs))
