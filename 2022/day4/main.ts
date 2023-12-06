const assignments = Deno.readTextFileSync("./assignments.in");

const assignArray = assignments.split("\n")
  // splits into assignment pairs
  .map((assignment) => assignment.split(","))
  // converts pair into [x: Number, y: Number]
  .map((pair) =>
    pair.map((assignment) => assignment.split("-").map((num) => Number(num)))
  );

const part1 = (function () {
  let counter = 0;
  assignArray.forEach(([elf1, elf2]) => {
    if (
      elf1[0] >= elf2[0] && elf1[1] <= elf2[1] ||
      elf2[0] >= elf1[0] && elf2[1] <= elf1[1]
    ) {
      counter++;
    }
  });
  return counter;
})();

const part2 = (function () {
  let counter = 0;
  assignArray.map((assignment) =>
    // converts range from each pair to Array<Number>
    assignment.map((pair) => {
      let newPair = [];
      for (let i = pair[0]; i <= pair[1]; i++) {
        newPair.push(i);
      }
      return newPair;
    })
  ).forEach((pair) => {
    // checks whether any numbers from pair[0] are in pair[1]
    // and increments counter if so
    let overlap = "";
    pair[0].forEach((section) => {
      if (pair[1].includes(section)) {
        overlap += section;
      }
    });

    if (overlap.length > 0) {
        counter++;
    }
  });

  return counter;
})();

console.log(`Part1: ${part1}`);
console.log(`Part2: ${part2}`);
