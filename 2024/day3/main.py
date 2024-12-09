from dataclasses import dataclass
from enum import Enum

class MulEnabler(Enum):
    Do = 0
    Dont = 1
    

@dataclass
class Mul:
    a: int
    b: int

    def eval(self) -> int:
        return self.a * self.b


def parse_mul(input: str, start_idx: int) -> tuple[Mul | None, int]:
    idx = start_idx
    for char in "mul(":
        if  input[idx] != char:
            return (None, idx)
        idx += 1

    num1 = ""
    for char in input[idx:]:
        if char.isnumeric():
            num1 += char
        else:
            break
        idx += 1
    if len(num1) == 0:
        return (None, idx)

    if input[idx] != ',':
        return (None, idx)
    idx += 1

    num2 = ""
    for char in input[idx:]:
        if char.isnumeric():
            num2 += char
        else:
            break
        idx += 1

    if input[idx] != ')':
        return (None, idx)
    idx += 1

    return (Mul(a=int(num1), b=int(num2)), idx)

def parse_do_dont(input: str, start_idx: int) -> tuple[MulEnabler | None, int]:
    do = "do()"
    dont = "don't()"
    if input[start_idx:start_idx + len(dont)] == dont:
        idx = start_idx + 6
        return (MulEnabler.Dont, idx)
    elif input[start_idx:start_idx + len(do)] == do:
        idx = start_idx + 3
        return (MulEnabler.Do, idx)
    else: return (None, start_idx)


def parse_input(input: str) -> list[Mul | MulEnabler]:
    insts: list[Mul | MulEnabler] = []
    last_parsed = 0
    for idx, char in enumerate(input):
        if idx < last_parsed:
            continue

        match char:
            case 'd':
                (parsed, new_idx) = parse_do_dont(input, idx)
                print(parsed)
            case 'm':
                (parsed, new_idx) = parse_mul(input, idx)
            case _: continue
            
        if parsed is not None:
            insts.append(parsed)
        last_parsed = new_idx

    return insts


with open("input.txt") as file:
    input = file.read()
    
    # Part 1
    part1 = map(lambda i: i.eval() if type(i) is Mul else 0, parse_input(input))
    part1 = sum(part1)
    print("part1:", part1)

    # Part 2
    insts = parse_input(input)
    resolved_insts: list[Mul] = []
    include = True
    for inst in insts:
        if type(inst) is MulEnabler:
            if inst == MulEnabler.Dont:
                include = False
            elif inst == MulEnabler.Do:
                include = True
            continue

        if type(inst) is Mul and include:
            resolved_insts.append(inst)

    part2 = map(lambda i: i.eval(), resolved_insts)
    part2 = sum(part2)
    print("part2:", part2)
        


