use core::slice;
use itertools::Itertools;

fn get_total_priority(priorities: Vec<String>) -> u32 {
    let priorities = priorities
        .iter()
        .map(|i| {
            i.chars()
                .map(|c| {
                    if c.is_lowercase() {
                        c as u32 - 96
                    } else {
                        c as u32 - 38
                    }
                })
                .collect_vec()
        })
        .collect_vec();

    priorities.iter().fold(0, |acc, i| {
        if i.len() == 1 {
            acc + i[0]
        } else {
            acc + i.iter().fold(0, |acc, i| acc + i)
        }
    })
}

fn part1(rucksacks: slice::Iter<&str>) -> u32 {
    let common_items: Vec<_> = rucksacks
        .map(|r| {
            let r = r.split_at(r.len() / 2);

            r.0.chars()
                .filter(|c| r.clone().1.contains(c.to_owned()))
                .unique()
                .collect::<String>()
        })
        .collect();

    get_total_priority(common_items)
}

fn part2(rucksacks: slice::Iter<&str>) -> u32 {
    let mut all_priorities: Vec<String> = Vec::new();

    for chunk in &rucksacks.chunks(3) {
        let group_members = chunk.collect_vec();
        let mut group: Vec<String> = Vec::new();
        for i in group_members[0].chars() {
            let i = i.to_string();
            if group_members[1].contains(&i) && group_members[2].contains(&i) && !group.contains(&i)
            {
                group.push(i);
            }
        }

        all_priorities.append(&mut group);
    }

    get_total_priority(all_priorities)
}

fn main() {
    let rucksacks = include_str!("rucksacks.in").split("\n").collect_vec();
    let rucksacks = rucksacks.iter();
    rucksacks.clone().for_each(|r| {
        if r.len() % 2 != 0 {
            panic!("Comparments aren't the same size");
        }
    });

    println!("{:?}", part1(rucksacks.clone()));
    println!("{:?}", part2(rucksacks));
}
