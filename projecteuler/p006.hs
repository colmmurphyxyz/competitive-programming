import Prelude

nats :: [Integer]
nats = 1 : map (1+) nats

-- Returns the sum of the first n Natural Numbers
sumOfNats :: Integral a => a -> a
sumOfNats n = n * (n + 1) `div` 2

squares :: [Integer]
squares = map (\n -> n * n) [1..]

-- Returns the sum of the first n squares
sumOfSquares :: Int -> Integer
sumOfSquares n = sum $ take n squares

square :: Num a => a -> a
square a = a * a

main :: IO ()
main = do
    let sumOf100NatsSquared = square $ sumOfNats 100
    let sumOf100Squares = sumOfSquares 100
    let difference = sumOf100NatsSquared - sumOf100Squares
    print sumOf100NatsSquared
    print sumOf100Squares
    print difference
