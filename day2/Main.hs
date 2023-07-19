module Main where

import Data.List.Split (splitOn)
import System.Environment (getArgs)

getPlays :: String -> [[String]]
getPlays file = map (splitOn " ") (lines file)

getWinner :: String -> String -> (Int, String)
getWinner p1 p2 = case (p1, p2) of
  ("C", "X") -> wins
  ("B", "Z") -> wins
  ("A", "Y") -> wins
  ("A", "X") -> draws
  ("B", "Y") -> draws
  ("C", "Z") -> draws
  _ -> loses
  where
    wins = (1, p2)
    draws = (-1, p2)
    loses = (0, p2)

getPoints :: [String] -> Int
getPoints play = case chosen of
  "X" -> 1 + playPoint
  "Y" -> 2 + playPoint
  "Z" -> 3 + playPoint
  where
    (winner, chosen) = getWinner (head play) (play !! 1)
    playPoint = case winner of
      -1 -> 3 -- won
      0 -> 0 -- lost
      1 -> 6 -- drew

-- only required for part 2
chooseMove :: [String] -> [String]
chooseMove [p1, p2] =
  [p1]
    <> [ case p2 of
           -- should lose
           "X" -> case p1 of
             "A" -> "Z"
             "B" -> "X"
             "C" -> "Y"
           -- should draw
           "Y" -> case p1 of
             "A" -> "X"
             "B" -> "Y"
             "C" -> "Z"
           -- should win
           "Z" -> case p1 of
             "A" -> "Y"
             "B" -> "Z"
             "C" -> "X"
       ]

main :: IO ()
main = do
  args <- getArgs
  file <- readFile (head args)
  let plays = chooseMove <$> getPlays file
  let points = fmap getPoints plays
  print . sum $ points
