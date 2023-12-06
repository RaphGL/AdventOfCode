with open("stacks.in", "r") as f:
    file = f.read()

    def parse_file():
        stacks = file[:287]

        def get_stackcol(col):
            column = 1 + (col - 1) * 4
            for i in range(column, len(stacks), 36):
                yield stacks[i]

        new_stack = ["" for _ in range(9)]
        for i in range(9):
            for j in get_stackcol(i+1):
                new_stack[i] += j
        new_stack = list(map(lambda x: x.strip(), new_stack))

        final_stack = []
        for s in new_stack:
            new_s = []
            for c in s:
                new_s.append(c)
            final_stack.append(list(reversed(new_s)))

        instructions = file[325:].splitlines()
        new_instructions = []
        for i in instructions:
            instruction = {}
            instruction["quantity"] = int(i[5:7])
            instruction["from"] = int(i[12:14].strip())
            instruction["to"] = int(i[17:].strip())
            new_instructions.append(instruction)

        return (final_stack, new_instructions)

    def part1(stacks, instructions):
        for i in instructions:
            for _ in range(i["quantity"]):
                stacks[i["to"]-1].append(stacks[i["from"]-1].pop())

        result = ""
        for i in stacks:
            result += i[-1]
        print(f"Part 1: {result}")

    def part2(stacks, instructions):
        for i in instructions:
            crates = []
            # errors out and am tired
            for _ in range(i["quantity"]):
                if stacks[i["from"]-1] != []:
                    crates.append(stacks[i["from"]-1].pop())
            if crates != []:
                stacks[i["to"]-1] += list(reversed(crates))

        result = ""
        for i in stacks:
            if i != []:
                result += i[-1]
        print(f"Part 1: {result}")
                
        


    (stacks, instructions) = parse_file()
    part1(stacks, instructions)
    part2(stacks, instructions)
