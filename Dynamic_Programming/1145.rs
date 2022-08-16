// Dynamic_Programming/1145.rs
// https://cses.fi/problemset/task/1145

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

	let mut answer: Vec<usize>= Vec::new();
	for x in x {
		if x > *answer.last().unwrap_or_else(|| &usize::MIN) { answer.push(x) }
		else {
			let pos = answer.partition_point(|&a| a < x);
			answer[pos] = x;
		}
	}
	println!("{}", answer.len());
}