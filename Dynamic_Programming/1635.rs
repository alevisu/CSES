// Dynamic_Programming/1635.rs

use std::io;
// const INF: usize = usize::pow(10, 10);
const MOD: usize = usize::pow(10, 9) + 7;

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
    
    let mut answer: Vec<usize> = vec![0; x+1];
    answer[0] = 1;

    for value in 1..=x {
        for coin in &coins {
            if value >= *coin {
                answer[value] = (answer[value] + answer[value - *coin]) % MOD;
            }
        }
    }

    println!("{}", answer[x])
}