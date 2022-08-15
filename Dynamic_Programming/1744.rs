// Dynamic_Programming/1744.rs
// https://cses.fi/problemset/task/1744

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
	let (mut width, mut height) = { let l = read_ints(2); (l[0], l[1]) };

	if width > height { let t = width; width = height; height = t} // ensure width is smaller
	let mut cuts = vec![vec![555; height+1]; width+1];
	for i in 1..=width { cuts[i][i] = 0 }

	for w in 1..=width {
		for h in 1..=height {
			for cut in 1..w { cuts[w][h] = min(cuts[w][h], 1 + cuts[cut][h] + cuts[w-cut][h]) }
			for cut in 1..h { cuts[w][h] = min(cuts[w][h], 1 + cuts[w][cut] + cuts[w][h-cut]) }
		}
	}

	println!("{}", cuts[width][height]);
}