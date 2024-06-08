import Text.Read

f :: Int -> [Int] -> Int
f k nums =
    let minimum = nums !! (k - 1)
    in length (filter (\x -> x >= minimum && x > 0) nums)

main :: IO ()
main = do
    input <- getLine
    let s = words input
    let k = read (head (tail s)) :: Int
    input <- getLine
    let nums = map read $ words input :: [Int]
    print $ f k nums
