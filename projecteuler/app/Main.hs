module Main (main) where

import P003(largestPrimeFactor)

main :: IO ()
main = do
    print $ largestPrimeFactor 600851475143
