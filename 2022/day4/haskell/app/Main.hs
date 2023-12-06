module Main where

import Data.List (intersect)
import Data.List.Split (splitOn)
import System.Environment (getArgs)
import Text.Printf (printf)

findIntersections :: ([Int] -> [Int] -> [Int] -> Bool) -> String -> Int
findIntersections checkIntersection file = foldr (\a -> if a then (+ 1) else id) 0 intersections
  where
    assignments =
      let intoRange [a1, a2] = [read a1 :: Int .. read a2 :: Int]
          assignments' = fmap (fmap $ splitOn "-") $ splitOn "," <$> lines file
       in fmap intoRange <$> assignments'

    assignmentsIntersect a = case a of
      [a1, a2] -> checkIntersection intersection a1 a2
        where
          intersection = a1 `intersect` a2
      [a] -> False
      [] -> False

    intersections = fmap assignmentsIntersect assignments

part1 :: [Int] -> [Int] -> [Int] -> Bool
part1 intersection a1 a2 = intersection == a1 || intersection == a2

part2 :: [Int] -> [Int] -> [Int] -> Bool
part2 intersection a1 a2 = not $ null intersection

main :: IO ()
main = do
  args <- getArgs
  file <- readFile $ head args
  printf "Part 1: %d\n" $ findIntersections part1 file
  printf "Part 2: %d\n" $ findIntersections part2 file
