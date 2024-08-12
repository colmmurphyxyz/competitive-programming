import Prelude

divisibleBy :: Integral a => a -> a -> Bool
divisibleBy n k = k `mod` n == 0

divisibleByAll :: Integral a => [a] -> a -> Bool
divisibleByAll list elem
    | null list = True
    | divisibleBy (head list) elem = divisibleByAll (tail list) elem
    | otherwise = False

multiplesOf20 :: [Int]
multiplesOf20 = 20 : map (+ 20) multiplesOf20

main :: IO ()
main = do
    print $ head $ filter (divisibleByAll [11 .. 20]) multiplesOf20