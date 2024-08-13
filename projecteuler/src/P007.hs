module P007(nthPrime, p007) where

import Utils(primes)

nthPrime :: Int -> Integer
nthPrime n = primes !! (n - 1) -- subtract one as lists are 0-indexed in Haskell

p007 :: Integer
p007 = nthPrime 10001