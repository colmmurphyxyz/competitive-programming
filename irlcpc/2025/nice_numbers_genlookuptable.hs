countNiceNumbers :: Int -> Int -> [Char] -> Int -> Int
countNiceNumbers n currLength curr bias
    | currLength == n = if abs bias `mod` 3 == 0 then 1 else 0
    | otherwise = sum [
        countNiceNumbers n (currLength + 1) (curr ++ "2") (bias + 2),
        countNiceNumbers n (currLength + 1) (curr ++ "3") bias,
        countNiceNumbers n (currLength + 1) (curr ++ "7") (bias + 1),
        countNiceNumbers n (currLength + 1) (curr ++ "9") bias
    ]

numbers :: Int -> Int -> Int -> Int
numbers n currLength bias
    | currLength == n = if abs bias `mod` 3 == 0 then 1 else 0
    | otherwise = sum [
        numbers n (currLength + 1) (bias + 2),
        2 * numbers n (currLength + 1) bias,
        numbers n (currLength + 1) (bias + 1)
    ]


main :: IO ()
main = do
    input <- getLine
    let n = read input :: Int
    print n
    print $ numbers n 0 0