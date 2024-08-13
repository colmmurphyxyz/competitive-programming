module P003(largestPrimeFactor, p003) where

import Prelude
import Utils(primeFactors)

largestPrimeFactor :: Int -> Int
largestPrimeFactor n = maximum $ primeFactors n

p003 :: Int
p003 = largestPrimeFactor 600851475143
