import Prelude

divisibleByNOrK :: Integer -> Integer -> [Integer]
divisibleByNOrK n k = 
    filter (\x -> x `mod` n == 0 || x `mod` k == 0) [1..]

main :: IO ()
main = do
    let answer = sum (takeWhile (<1000) (divisibleByNOrK 3 5))
    print answer -- 233168
