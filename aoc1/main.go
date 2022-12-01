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

func findBiggestCalories(calories []int) int {
	var biggest int
	for _, cal := range calories {
		if cal > biggest {
			biggest = cal
		}
	}
	return biggest
}

func main() {
	elves := convertToElves("./elves.txt")
	calSum := sumCalories(elves)
	fmt.Println("The elf with the most calories has:", findBiggestCalories(calSum), "calories")
}
