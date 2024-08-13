module P003(largestPrimeFactor, p003) where

import Prelude

primeFactors :: Int -> [Int]
primeFactors n =
    case factors of
        [] -> [n]
        _  -> factors ++ primeFactors (n `div` head factors)
    where factors = take 1 $ filter (\x -> (n `mod` x) == 0) [2 .. n-1]

largestPrimeFactor :: Int -> Int
largestPrimeFactor n = maximum $ primeFactors n

p003 :: Int
p003 = largestPrimeFactor 600851475143
