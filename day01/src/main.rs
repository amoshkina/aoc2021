use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn part1() -> i32 {
    let filename = "./input.txt";
    let mut prev_depth = -1;
    let mut increase_counter = 0;

    if let Ok(lines) = read_lines(filename) {
        for line in lines {
            if let Ok(string) = line {
                let current_depth = string.parse::<i32>().unwrap();
                if current_depth > prev_depth {
                    increase_counter = increase_counter + 1;
                }
                prev_depth = current_depth;
            }
        }
    }

    increase_counter - 1
}

fn part2() -> i32 {
    let filename = "./input.txt";
    let mut vec: Vec<i32> = Vec::new();

    if let Ok(lines) = read_lines(filename) {
        for line in lines {
            if let Ok(string) = line {
                let current_depth = string.parse::<i32>().unwrap();
                vec.push(current_depth);
            }
        }
    }

    if vec.len() < 3 {
        return 0;
    }
    let mut idx = 2;
    let mut prev_depth = -1;
    let mut increase_counter = 0;

    while idx < vec.len() {
        let current_depth = vec[idx] + vec[idx-1] + vec[idx-2];
        if current_depth > prev_depth {
            increase_counter += 1;
        }
        prev_depth = current_depth;
        idx += 1;
    }

    increase_counter - 1
}

fn main()  {
    println!("Day 01.1: {}", part1());
    println!("Day 01.2: {}", part2());
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}