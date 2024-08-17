import Text.Read

f :: Int -> String
f x
    | x == 2 = "NO"
    | even x = "YES"
    | otherwise = "NO"

main :: IO ()
main = do
    input <- getLine
    case readMaybe input :: Maybe Int of
        Just number -> putStrLn $ f number
        Nothing -> putStrLn "Invalid input"
