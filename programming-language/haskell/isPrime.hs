-- Determine if a natural number is prime.

isPrime :: Int -> Bool
isPrime x = if x == 1 then True else null [k | k <- [2..isqrt x], x `mod` k == 0]
    where isqrt = floor . sqrt . fromIntegral
