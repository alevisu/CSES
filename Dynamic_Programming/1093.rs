// Dynamic_Programming/1093.rs
// https://cses.fi/problemset/task/1093

use std::io;//{io, cmp::max};
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
	let n = read_ints(1)[0];
	
	if (n*(n+1)/2)&1 == 1 { println!("0"); return }
	
	let target = n*(n+1)/4;
	let mut ways = vec![0usize; target+1];
	ways[0] = 1;
	for number in 1..n { 
		let prev = ways.to_vec();
		for sum in number..=target {
			ways[sum] = 
				if sum < number {	prev[sum]	% MOD } 
				else { (prev[sum] + prev[sum-number]) % MOD }
		}
	}

	println!("{}", ways[target])

}