import Prelude

fib :: [Integer]
fib = 1 : nxt
    where nxt = 2 : zipWith (+) fib nxt

evenFib :: [Integer]
evenFib = filter even fib

main :: IO ()
main = do
    print $ sum (takeWhile (<4_000_000) evenFib)

