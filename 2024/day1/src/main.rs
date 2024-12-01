use std::collections::HashMap;

static INPUT: &str = include_str!("input.txt");

fn convert_to_tuples(input: &str) -> Vec<(usize, usize)> {
    let input = input.trim();
    let mut locations_1 = Vec::new();
    let mut locations_2 = Vec::new();

    input.split('\n').for_each(|line| {
        let mut line = line.split_whitespace();
        let loc1 = line.next().unwrap().parse::<usize>().unwrap();
        let loc2 = line.next().unwrap().parse::<usize>().unwrap();
        locations_1.push(loc1);
        locations_2.push(loc2);
    });

    locations_1.sort();
    locations_2.sort();

    locations_1.into_iter().zip(locations_2).collect()
}

fn part1(locations: &Vec<(usize, usize)>) -> usize {
    locations
        .iter()
        .map(|(first, second)| first.abs_diff(*second))
        .sum()
}

fn part2(locations: &Vec<(usize, usize)>) -> usize {
    let mut occurrences: HashMap<usize, usize> = HashMap::new();

    for (_, num) in locations {
        occurrences.entry(*num).or_default();
        let occurrence = occurrences.get_mut(num).unwrap();
        *occurrence += 1;
    }

    occurrences = occurrences.into_iter().collect();

    locations
        .iter()
        .map(|(num, _)| {
            if !occurrences.contains_key(num) {
                0
            } else {
                num * occurrences[num]
            }
        })
        .sum()
}

fn main() {
    let locations = convert_to_tuples(INPUT);
    println!("part 1: {}", part1(&locations));
    println!("part 2: {}", part2(&locations));
}
