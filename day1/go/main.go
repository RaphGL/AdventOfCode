package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func convertToElves(filepath string) [][]int {
	f, err := os.ReadFile(filepath)
	if err != nil {
		panic("Could not read elves file")
	}

	file := strings.Split(string(f), "\n\n")
	elves := [][]int{}
	//  populates the elves slice of slices
	for _, line := range file {
		// converts string to a slice of ints
		calories := strings.Split(line, "\n")
		intcal := []int{}
		for _, c := range calories {
			c, err := strconv.Atoi(c)
			if err != nil {
				panic(err)
			}
			intcal = append(intcal, c)
		}
		elves = append(elves, intcal)
	}

	return elves
}

func sumCalories(elves [][]int) []int {
	totalCalories := []int{}
	for _, elf := range elves {
		sum := 0
		for _, cal := range elf {
			sum += cal
		}
		totalCalories = append(totalCalories, sum)
	}
	return totalCalories
}

func findBiggestCalories(calories []int) [3]int {
	var biggest [3]int
	for i := 0; i < 3; i++ {
		highestVal := 0
		for _, cal := range calories {
			if i == 0 && cal > highestVal {
				highestVal = cal
			} else if i > 0 && cal > highestVal && cal < biggest[i-1] {
				highestVal = cal
			}
		}
		biggest[i] = highestVal
	}
	return biggest
}

func main() {
	elves := convertToElves("./elves.txt")
	elfCalSum := sumCalories(elves)
	biggestCals := findBiggestCalories(elfCalSum)
	fmt.Println("Elf calories rank:\n1.", biggestCals[0], "\n2.", biggestCals[1], "\n3.", biggestCals[2])
	fmt.Println("Total calories:", biggestCals[0]+biggestCals[1]+biggestCals[2])
}
