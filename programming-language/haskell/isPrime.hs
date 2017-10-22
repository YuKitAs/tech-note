-- Determine if a natural number is prime.

isPrime :: Int -> Bool
isPrime x
    | x == 1 = True
    | otherwise = null [k | k <- [2..isqrt x], x `mod` k == 0] where isqrt = floor . sqrt . fromIntegral
