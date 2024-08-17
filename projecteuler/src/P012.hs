module P012(p012) where

triangleNumbers :: [Integer]
triangleNumbers = scanl (+) 1 [2..]

factors :: Integral a => a -> [a]
factors n = filter (\x -> n `mod` x == 0) [1..n]

p012 :: Integer
p012 = do
    let triangleNumberFactors = map factors triangleNumbers
    let moreThan500Divisors = dropWhile (\x -> length x < 500) triangleNumberFactors
    last $ head moreThan500Divisors
    