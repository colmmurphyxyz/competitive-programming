import Prelude

primeFactors :: Int -> [Int]
primeFactors n =
    case factors of
        [] -> [n]
        _  -> factors ++ primeFactors (n `div` head factors)
    where factors = take 1 $ filter (\x -> (n `mod` x) == 0) [2 .. n-1]

main :: IO ()
main = do
    print $ primeFactors 13195
    print $ primeFactors 600851475143