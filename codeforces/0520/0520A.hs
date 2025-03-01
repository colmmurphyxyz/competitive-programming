import Data.Char(toLower)

isPanagram :: String -> Bool
isPanagram xs = all (`elem` xs) ['a'..'z'] 

formatOutput :: Bool -> String
formatOutput b
    | b = "YES"
    | otherwise = "NO"

main :: IO ()
main = do
    n <- getLine
    input <- getLine
    let word = map toLower input
    putStrLn $ formatOutput (isPanagram word)