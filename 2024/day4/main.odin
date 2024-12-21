package main

import "core:fmt"
import "core:strings"
import "core:os"

Direction :: enum {
	Vertical,
	Horizontal,
	Diagonal,
}

count_occurrences :: proc(dir: Direction, input, word: string) -> int {
	total: int
	count: int

	switch dir {
		case .Horizontal:
			for i in 0..<len(input)-len(word) {
				curr_word := input[i:i+len(word)]
				if curr_word == word {
					count += 1
				}

				rev_curr_word := strings.reverse(curr_word) or_continue
				if rev_curr_word == word {
					count += 1
				}
				delete(rev_curr_word)
			}

		case .Vertical:
			lines, err := strings.split_lines(input)
			if err != .None {
				fmt.println("failed to split line")
				return count
			}
			defer delete(lines)

			curr_word := make([]u8, len(word))
			defer delete(curr_word)

			for y in 0..<len(lines)-len(word) {
				for x in 0..<len(lines[y]) {
					for i in 0..<len(word) {
						curr_word[i] = lines[y+i][x]
					}

					curr_word_str := cast(string)curr_word
					if curr_word_str == word {
						count += 1
					}

					rev_curr_word := strings.reverse(curr_word_str) or_continue
					if rev_curr_word == word {
						count += 1
					}
				}
			}

		case .Diagonal:
			lines, err := strings.split_lines(input)
			if err != .None {
				fmt.println("failed to split line")
				return count
			}
			defer delete(lines)

			curr_word := make([]u8, len(word))
			defer delete(curr_word)

			for y in 0..<len(lines)-len(word) {
				for x in 0..<len(lines[y]) {
					if x + len(word) <= len(lines[y]) {
						for i in 0..<len(word) {
							curr_word[i] = lines[y+i][x+i]
						}

						curr_word_str := cast(string)curr_word
						if curr_word_str == word {
							count += 1
						}

						rev_curr_word := strings.reverse(curr_word_str) or_continue
						if rev_curr_word == word {
							count += 1
						}
					}

					if x - len(word) + 1 >= 0 {
						for i in 0..<len(word) {
							curr_word[i] = lines[y+i][x-i]
						}

						curr_word_str := cast(string)curr_word
						if curr_word_str == word {
							count += 1
						}

						rev_curr_word := strings.reverse(curr_word_str) or_continue
						if rev_curr_word == word {
							count += 1
						}
					}
				}
			}
	}

	return count
}

cross_occurrences :: proc(input, word: string)  -> int{
	count: int
	lines, err := strings.split_lines(input)
	if err != .None {
		fmt.println("failed to split line")
		return count
	}
	defer delete(lines)

	curr_word_left := make([]u8, len(word))
	curr_word_right := make([]u8, len(word))
	defer delete(curr_word_left)
	defer delete(curr_word_right)

	for y in 0..<len(lines)-len(word) {
		for x in 0..<len(lines[y]) {
			if x + len(word) - 2 <= len(lines[y]) && x - len(word) + 1 >= 0 {
				// it's xmas if it's at least == 2
				xmas_factor: int

				for i in 0..<len(word) {
					curr_word_left[i] = lines[y+i][x-i]
					curr_word_right[i] = lines[y+i][x+i-len(word)+1]
				}

				left_str := cast(string)curr_word_left
				right_str := cast(string)curr_word_right

				rev_left := strings.reverse(left_str)
				defer delete(rev_left)
				rev_right := strings.reverse(right_str)
				defer delete(rev_right)

				if left_str == word || rev_left == word {
					xmas_factor += 1
				}

				if right_str == word || rev_right == word {
					xmas_factor += 1
				}

				if xmas_factor >= 2 {
					count += 1
				}

				fmt.println(left_str, right_str)
			}
		}
	}

	return count
	
}

part1 :: proc(input: string) -> int {
	horizontal_occurs := count_occurrences(.Horizontal, input, "XMAS")	
	vertical_occurs := count_occurrences(.Vertical, input, "XMAS")
	diagonal_occurs := count_occurrences(.Diagonal, input, "XMAS")
	return horizontal_occurs + vertical_occurs + diagonal_occurs
}

part2 :: proc(input: string) -> int {
	return cross_occurrences(input, "MAS")

}

main :: proc() {
	file_bytes, success := os.read_entire_file_from_filename("input.txt")
	if !success {
		fmt.println("failed to read file: inputs.txt")
		return
	}
	defer delete(file_bytes)

	input := cast(string)file_bytes

	fmt.println("part 1:", part1(input))
	fmt.println("part 2:", part2(input))
}
