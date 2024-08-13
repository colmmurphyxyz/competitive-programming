module P004(largestPalindromeProductInRange, p004) where

import Prelude

reverseInt :: Integer -> Integer
reverseInt = read . reverse . show

isPalindrome :: Integer -> Bool
isPalindrome n = n == reverseInt n

-- Pair an element with every member of the input list
pairElement:: a -> [a] -> [] (a,a)
pairElement element list =
    case list of
        [] -> []
        x:xs -> (element, x) : pairElement element xs

-- Make all possible pairs of elements in a given list
makePairs :: [] a -> [] (a, a)
makePairs list =
    case list of
        [] -> []
        (x:xs) -> pairElement x xs ++ makePairs xs

makePairsInts :: [Integer] -> [(Integer, Integer)]
makePairsInts = makePairs

tupleProduct :: (Integer, Integer) -> Integer
tupleProduct (a, b) = a * b

largestPalindromeProductInRange :: Integer -> Integer -> Integer
largestPalindromeProductInRange a b =
    maximum . filter isPalindrome $ map tupleProduct (makePairsInts [a .. b])

p004 :: Integer
p004 = largestPalindromeProductInRange 100 999