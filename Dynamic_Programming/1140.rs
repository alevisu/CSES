// Dynamic_Programming/1140.rs
// https://cses.fi/problemset/task/1140

use std::{io, cmp::max, collections::BTreeMap};

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
	let mut projects: Vec<Vec<usize>> = Vec::new();
	for _ in 0..n { projects.push(read_ints(3)) }
	
	projects.sort_by_key(|p| p[1]);
	let mut rewards: BTreeMap<usize, usize> = BTreeMap::new();
	rewards.insert(0, 0);
	let mut max_reward = 0;

	for p in &projects {
		let best_reward_with_current_project = rewards.range(0..p[0]).last().unwrap().1 + p[2];
		max_reward = max(max_reward, best_reward_with_current_project);
		rewards.insert(p[1], max_reward);
	}
	
	println!("{:?}", max_reward);
	
}