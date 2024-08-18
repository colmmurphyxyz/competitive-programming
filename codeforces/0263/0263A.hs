import Control.Monad(replicateM)
import Data.Char(digitToInt)
import Data.List (elemIndex)

findRowWithOne :: [Int] -> Int
findRowWithOne xs = case elemIndex 1 xs of
    Just idx -> idx
    Nothing -> error "Something has gone terribly wrong"

findOneIndex :: [Int] -> Int
findOneIndex xs= case elemIndex 1 xs of
    Just idx -> idx
    Nothing -> error "Something has gone horrible wrong"

findOne :: [[Int]] -> (Int, Int)
findOne rows = do
    let rowIndex = findRowWithOne $ map sum rows
    let colIndex = findOneIndex $ rows !! rowIndex
    (rowIndex, colIndex)

solution :: [[Int]] -> Int
solution rows =
    let
        coords = findOne rows
        distance = (abs (2 - fst coords), abs (2 - snd coords))
    in
    uncurry (+) distance


main :: IO ()
main = do
    input <- replicateM 5 getLine
    let rowsString = map words input
    let rows = map (map (digitToInt . head)) rowsString
    print $ solution rows
