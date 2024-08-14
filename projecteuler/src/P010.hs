module P010(sumOfPrimes, p010) where

import Utils(primes)

-- Outputs the sum of all prime numbers less than a given limit
sumOfPrimes :: Integer -> Integer
sumOfPrimes n = sum $ takeWhile (<n) primes

p010 :: Integer
p010 = sumOfPrimes 2000000