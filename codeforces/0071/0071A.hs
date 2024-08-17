import Text.Read
import Control.Monad (replicateM)

shortform :: String -> String
shortform s
    | length s <= 10 = s
    | otherwise = [head s] ++ show (length s - 2) ++ [last s]

main :: IO ()
main = do
    n <- readLn
    lines <- replicateM n getLine
    putStrLn . unlines . map shortform $ lines
