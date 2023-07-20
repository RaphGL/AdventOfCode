module Main where

import Data.Char (isLower, ord)
import Data.List (intersect, nub)
import Data.List.Split (chunksOf)
import System.Environment (getArgs)
import Text.Printf (printf)

getTotalPriority :: [String] -> Int
getTotalPriority rucksacks = sum $ fmap sum priorities
  where
    getPriority l =
      if isLower l
        then ord l - 96
        else ord l - 38
    priorities = fmap (fmap getPriority) rucksacks

part1 :: [String] -> Int
part1 rucksacks = getTotalPriority intersectingRucksacks
  where
    splitRucksacks = fmap (\r -> let half = length r `div` 2 in splitAt half r) rucksacks
    intersectingRucksacks = nub <$> fmap (uncurry intersect) splitRucksacks

part2 rucksacks =
  let rucksackChunks = chunksOf 3 rucksacks
   in getTotalPriority $ nub <$> fmap (\[x, y, z] -> x `intersect` (y `intersect` z)) rucksackChunks

main :: IO ()
main = do
  args <- getArgs
  file <- readFile (head args)
  let rucksacks = lines file
  if not $ any (odd . length) rucksacks
    then do
      printf "Part 1: %d\n" $ part1 rucksacks
      printf "Part 2: %d\n" $ part2 rucksacks
    else putStrLn "Compartments aren't the same size"
