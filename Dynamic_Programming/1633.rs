// Dynamic_Programming/1633.rs

use std::io;

const M: usize = usize::pow(10, 9) + 7;
const MAX_N: usize = usize::pow(10, 6);

fn main() {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).unwrap();

    let n = buffer.trim().parse::<usize>().unwrap();

    let mut combs: [usize; MAX_N + 1] = [0; MAX_N + 1];
    combs[0] = 1;
    for i in 1..=n {
        for j in 1..=6 {
            if i >= j { combs[i] = (combs[i] + combs[i-j]) % M }
        }
    }
    print!("{:?}\n", combs[n]);
}