// Dynamic_Programming/1653.rs
// https://cses.fi/problemset/task/1653

use std::{io, cmp::min};

fn read_ints(quantity: usize) -> Vec<usize> {
	let mut line = String::new();
	io::stdin().read_line(&mut line).expect("No input provided");
	let res: Vec<usize> = line.trim().split(char::is_whitespace)
	.map(|s| s.parse().expect("Can't parse this!")).collect();
	if res.len() != quantity { panic!("Wrong quantity of numbers in line") };
	res
}

fn main() {
	let (n, max_weight) = { let v = read_ints(2); (v[0], v[1]) };
	let weight = read_ints(n);

	let mut best = vec![(1337, 0); 1<<n];
	best[0] = (1, 0);

	for rides in 1..1<<n { for person in 0..n {
		if rides & (1<<person) == 0 { continue }
		let mut option = best[(1<<person)^rides];
		if option.1 + weight[person] <= max_weight { option.1 += weight[person] }
		else { option = (option.0+1, weight[person]) }
		best[rides] = min(best[rides], option)
	}}

	println!("{}", best[(1<<n)-1].0)
}