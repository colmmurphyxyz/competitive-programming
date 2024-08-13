module P002(sumOfEvenFibonacciNumbers, p002) where

import Prelude
import Utils(fibonaccis)

-- This problem takes the fibonacci sequence as 1, 2, 3, 5, 8, 13, ...
fib :: [Integer]
fib = tail . tail $ fibonaccis

evenFib :: [Integer]
evenFib = filter even fib

-- Returns the sum of all *even* Fibonacci numbers up to some limit passed as an argument
sumOfEvenFibonacciNumbers :: Integer -> Integer
sumOfEvenFibonacciNumbers n =
    sum (takeWhile (<n) evenFib)

p002 :: Integer
p002 = sumOfEvenFibonacciNumbers 4000000

