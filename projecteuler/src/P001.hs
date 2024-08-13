module P001(sumOfMultiplesOf3Or5LessThan, p001) where

import Prelude

divisibleByNOrK :: Integer -> Integer -> [Integer]
divisibleByNOrK n k = 
    filter (\x -> x `mod` n == 0 || x `mod` k == 0) [1..]

sumOfMultiplesOf3Or5LessThan :: Integer -> Integer
sumOfMultiplesOf3Or5LessThan n =
    sum (takeWhile (<n) (divisibleByNOrK 3 5))

p001 :: Integer
p001 = sumOfMultiplesOf3Or5LessThan 1000
