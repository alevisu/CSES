// Dynamic_Programming/1634.rs

use std::{io, cmp::min, convert::TryInto};
const INF: usize = usize::pow(10, 10);

fn read_ints(quantity: usize) -> Vec<usize> {
    let mut line = String::new();
    io::stdin().read_line(&mut line).expect("No input provided");
    let res: Vec<usize> = line.trim().split(char::is_whitespace)
        .map(|s| s.parse().expect("Can't parse this!")).collect();
    if res.len() != quantity { panic!("Wrong quantity of numbers in line") };
    res
}

fn main() {
    let (n, x) = { let l = read_ints(2); (l[0], l[1]) };
    let coins = read_ints(n); 
    
    let mut answer: Vec<usize> = vec![INF; x+1];
    for c in &coins { if *c <= x { answer[*c] = 1; } }
    answer[0] = 0;

    for value in 1..=x {
        for option in &coins {
            if value >= *option {
                answer[value] = min(answer[value], answer[value - *option] + 1);
            }
        }
    }

    println!("{}", if answer[x] != INF { answer[x].try_into().unwrap() } else { -1 })
}