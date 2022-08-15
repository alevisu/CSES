// Dynamic_Programming/1097.rs
// https://cses.fi/problemset/task/1097

use std::{io, cmp::max};

fn read_ints(quantity: usize) -> Vec<isize> {
	let mut line = String::new();
	io::stdin().read_line(&mut line).expect("No input provided");
	let res: Vec<isize> = line.trim().split(char::is_whitespace)
	.map(|s| s.parse().expect("Can't parse this!")).collect();
	if res.len() != quantity { panic!("Wrong quantity of numbers in line") };
	res
}

fn main() {
	let n = read_ints(1)[0] as usize;
	let x = read_ints(n);
	let (mut diff, mut total) = (vec![vec![0isize; n]; n], 0);
	for i in 0..n {	total += x[i]; diff[i][i] = x[i];	}
	for left in (0..n).rev() { for right in left+1..n {
		diff[left][right] = max(x[left]-diff[left+1][right], x[right]-diff[left][right-1])
	}}
	println!("{}", (total + diff[0][n-1])/2)
}