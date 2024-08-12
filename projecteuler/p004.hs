import Prelude

reverseInt :: Integer -> Integer
reverseInt = read . reverse . show

isPalindrome :: Integer -> Bool
isPalindrome n = n == reverseInt n

-- Pair an element with every member of the input list
pairElement:: a -> [a] -> [] (a,a)
pairElement elem list =
    case list of
        [] -> []
        x:xs -> (elem, x) : pairElement elem xs

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

main :: IO ()
main = do
    print $ maximum . filter isPalindrome $ map tupleProduct (makePairsInts [100 .. 999])