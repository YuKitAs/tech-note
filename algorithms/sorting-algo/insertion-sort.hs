-- Insertion sort in Haskell

insertSort :: [Int] -> [Int]
insertSort [] = []
insertSort (x:xs) = insert x (insertSort xs)
                    where insert y [] = [y]
                          insert y (x:xs) = if y > x then x:(insert y xs) else y:x:xs

-- An alternative with foldr
insertSort :: [Int] -> [Int]
insertSort [] = []
insertSort xs = foldr insert [] xs
                where insert y [] = [y]
                      insert y (x:xs) = if y > x then x:(insert y xs) else y:x:xs
