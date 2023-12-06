import regex as re

INPUTS = ""
with open("test", "r") as f:
    INPUTS = f.read().strip().splitlines()

def sum_calibrations(inputs):
        calibrations = []
        for input in inputs:
            numbers = filter(lambda c: c.isnumeric(), input)
            numbers = "".join(numbers)
            if numbers == "": continue

            calibration = int(numbers[0] + numbers[-1])
            calibrations.append(calibration)
        return sum(calibrations)

part1 = sum_calibrations


if __name__ == "__main__":
    print(f"Part 1: {part1(INPUTS)}")
