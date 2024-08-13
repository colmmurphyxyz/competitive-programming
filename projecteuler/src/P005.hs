module P005(divisibleByAll, firstDivisibleByAll, p005) where

import Prelude
import Utils(multiples)

divisibleBy :: Integral a => a -> a -> Bool
divisibleBy n k = k `mod` n == 0

divisibleByAll :: Integral a => [a] -> a -> Bool
divisibleByAll list element
    | null list = True
    | divisibleBy (head list) element = divisibleByAll (tail list) element
    | otherwise = False

firstDivisibleByAll :: Integral a => [a] -> [a] -> a
firstDivisibleByAll divisors candidates =
    let
        maxDivisor = maximum divisors
        maxDivisorMultiples = multiples maxDivisor
    in
    head $ filter (divisibleByAll divisors) (filter (`elem` maxDivisorMultiples) candidates)

p005 :: Integer
p005 = firstDivisibleByAll [11..19] (multiples 20)
