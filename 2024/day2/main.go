package main

import (
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func getReports(input string) ([][]int, error) {
	reportStrs := strings.Split(strings.TrimSpace(input), "\n")
	var reports [][]int

	for _, report := range reportStrs {
		report = strings.TrimSpace(report)
		levelStrs := strings.Split(report, " ")

		var levels []int
		for _, level := range levelStrs {
			levelInt, err := strconv.Atoi(level)
			if err != nil {
				return nil, err
			}

			levels = append(levels, levelInt)
		}

		reports = append(reports, levels)
	}

	return reports, nil
}

func reportIsSafe(report []int) bool {
	increases := report[0] < report[1]
	for i := 0; i < len(report)-1; i++ {
		diff := report[i+1] - report[i]
		if diff < 0 {
			diff = -diff
		}

		if diff < 1 || diff > 3 {
			return false
		}

		if report[i] == report[i+1] {
			return false
		}

		if increases && report[i] > report[i+1] {
			return false
		}

		if !increases && report[i] < report[i+1] {
			return false
		}
	}

	return true
}

func part1(reports [][]int) int {
	count := 0
	for _, report := range reports {
		if reportIsSafe(report) {
			count++
		}
	}

	return count
}

func part2(reports [][]int) int {
	count := 0
	for _, report := range reports {
		if reportIsSafe(report) {
			count++
			continue
		}

		for i := 0; i < len(report); i++ {
			reportWithoutLevel := make([]int, len(report))
			copy(reportWithoutLevel, report)
			reportWithoutLevel = slices.Delete(reportWithoutLevel, i, i+1)

			if reportIsSafe(reportWithoutLevel) {
				count++
				break
			}
		}
	}

	return count
}

func main() {
	inputFile, err := os.ReadFile("input.txt")
	if err != nil {
		fmt.Println(err)
		return
	}
	input := string(inputFile)

	reports, err := getReports(input)
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Println("part1:", part1(reports))
	fmt.Println("part2:", part2(reports))
}
