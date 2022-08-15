// Dynamic_Programming/1745.rs
// https://cses.fi/problemset/task/1745

use std::io;

fn read_ints(quantity: usize) -> Vec<usize> {
	let mut line = String::new();
	io::stdin().read_line(&mut line).expect("No input provided");
	let res: Vec<usize> = line.trim().split(char::is_whitespace)
	.map(|s| s.parse().expect("Can't parse this!")).collect();
	if res.len() != quantity { panic!("Wrong quantity of numbers in line") };
	res
}

fn main() {
	let n = read_ints(1)[0];
	let x = read_ints(n);
	
	let max_sum = x.iter().sum::<usize>();
	let mut sums = vec![0; max_sum + 1];
	sums[0] = 1;

	for x in x {
		for i in (x..=max_sum).rev() {
			sums[i] |= sums[i-x];
		}
	}

	println!("{}", sums.iter().sum::<usize>()-1);
	for i in 1..=max_sum {
		if sums[i] != 0 { print!("{} ", i) }
	}
}