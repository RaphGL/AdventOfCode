module Main where

import Data.List (sort)
import Data.List.Split
import System.Environment (getArgs)
import Text.Printf (printf)

getCaloriesPerElf :: String -> [Int]
getCaloriesPerElf calories = map (sum . map read . lines) $ splitOn "\n\n" calories

elfWithMostCalories :: String -> Int
elfWithMostCalories = maximum . getCaloriesPerElf

elfTop3MostCalories :: String -> [Int]
elfTop3MostCalories = take 3 . reverse . sort . getCaloriesPerElf

main :: IO ()
main = do
  args <- getArgs
  elvesCalories <- readFile (head args)
  printf "Elf with most calories: %d\n\n" $ elfWithMostCalories elvesCalories
  let top3 = elfTop3MostCalories elvesCalories
  printf "Top 3 Most Calories: %d\n" $ sum top3
