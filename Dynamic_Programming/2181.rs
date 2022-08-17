// Dynamic_Programming/2181.rs
// https://cses.fi/problemset/task/2181

use std::io;
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
	let (n, m) = { let v = read_ints(2); (v[0], v[1]) };
	
	let mut dp = vec![0; 1<<n];
	dp[(1<<n)-1] = 1;
	for _ in 0..=m { for i in 0..n {
		let mut t = vec![0; 1<<n];
		for k in 0..1<<n { 
			t[k] = (t[k] + dp[k^1<<i]) % MOD; 
			if i>0 && k>>i&1==1 && k>>i-1&1==1 { t[k] = (t[k] + dp[k^1<<i-1]) % MOD; }
		} dp = t;
	}}
	println!("{}", dp[0]);
}