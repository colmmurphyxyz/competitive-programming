module Utils(
    fibonaccis,
    multiples,
    primeFactors,
    primes
    ) where

fibonaccis :: [Integer]
fibonaccis = 0 : nxt
    where nxt = 1 : zipWith (+) fibonaccis nxt

multiples :: (Num a, Enum a) => a -> [a]
multiples n = map (*n) [1..]

primeFactors :: Int -> [Int]
primeFactors n =
    case factors of
        [] -> [n]
        _  -> factors ++ primeFactors (n `div` head factors)
    where factors = take 1 $ filter (\x -> (n `mod` x) == 0) [2 .. n-1]

primes :: [Integer]
primes = 2: 3: calcNextPrimes (tail primes) [5, 7 .. ]
  where
    calcNextPrimes (p:ps) candidates =
      let (smallerSquareP, _:biggerSquareP) = span (< p * p) candidates in
      smallerSquareP ++ calcNextPrimes ps [c | c <- biggerSquareP, rem c p /= 0]
