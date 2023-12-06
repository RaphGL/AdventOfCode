with open("./datastream.in", "r") as f:
    datastream = f.read().strip()
    def part1():
        for i in range(len(datastream)):
            if i < 4:
                continue
            if len(set(datastream[i-4:i])) == 4:
                return i

    def part2():
        for i in range(len(datastream)):
            if i < 14:
                continue
            if len(set(datastream[i-14:i])) == 14:
                return i

    
    print(part1())
    print(part2())