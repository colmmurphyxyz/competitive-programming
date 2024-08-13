module P002(sumOfEvenFibonacciNumbers, p002) where

import Prelude

fib :: [Integer]
fib = 1 : nxt
    where nxt = 2 : zipWith (+) fib nxt

evenFib :: [Integer]
evenFib = filter even fib

-- Returns the sum of all *even* Fibonacci numbers up to some limit passed as an argument
sumOfEvenFibonacciNumbers :: Integer -> Integer
sumOfEvenFibonacciNumbers n =
    sum (takeWhile (<n) evenFib)

p002 :: Integer
p002 = sumOfEvenFibonacciNumbers 4000000

