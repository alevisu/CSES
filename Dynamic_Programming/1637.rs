// Dynamic_Programming/1637.rs

use std::{io, cmp::min};
const INF: usize = usize::pow(10, 10);
// const MOD: usize = usize::pow(10, 9) + 7;

fn read_ints(quantity: usize) -> Vec<usize> {
    let mut line = String::new();
    io::stdin().read_line(&mut line).expect("No input provided");
    let res: Vec<usize> = line.trim().split(char::is_whitespace)
        .map(|s| s.parse().expect("Can't parse this!")).collect();
    if res.len() != quantity { panic!("Wrong quantity of numbers in line") };
    res
}

fn digits(mut number: usize) -> Vec<usize> {
    let mut rv = Vec::new();
    while number > 0 {
        rv.push(number % 10);
        number /= 10;
    }
    rv
}

fn main() {
    let n = read_ints(1)[0];

    let mut answer = vec![INF; n+1];
    answer[0] = 0;
    for number in 1..=n {
        for digit in &digits(number) {
            // println!("{:?}: {:?}", digit, digits(number));
            answer[number] = min(answer[number], answer[number-digit]+1);
        }
    }

    println!("{:?}", answer[n])
}