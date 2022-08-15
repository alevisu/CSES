// Dynamic_Programming/1746.rs
// https://cses.fi/problemset/task/1746

use std::io;//{io, cmp::max};
const MOD: u64 = u64::pow(10, 9) + 7;

fn read_ints(quantity: usize) -> Vec<usize> {
	let mut line = String::new();
	io::stdin().read_line(&mut line).expect("No input provided");
	let res: Vec<usize> = line.trim().split(char::is_whitespace)
		.map(|s| s.parse().expect("Can't parse this!")).collect();
	if res.len() != quantity { panic!("Wrong quantity of numbers in line") };
	res
}


fn main() {
	let (n, m) = { let l = read_ints(2); (l[0], l[1])};
	let x = read_ints(n);

	let mut answer = vec![vec![0u64; m+2]; n];
	for pos in 0..n { if x[pos] != 0 {answer[pos][x[pos]] = 1 }} // 1 means that value is on path, 0 - its not
	if x[0] == 0 { // in case first path value is unknown - mark all as viable
		for value in 1..=m { answer[0][value] = 1 }
	} 
	for pos in 1..n {
		let fixed_value = x[pos];
		if fixed_value == 0 { // value is not fixed
			for value in 1..=m {
				answer[pos][value]=(answer[pos-1][value-1] + answer[pos-1][value] + answer[pos-1][value+1]) % MOD;
			}
		} else { // path must go through this, so we have to discard all other results
			answer[pos][fixed_value]=(answer[pos-1][fixed_value-1] + answer[pos-1][fixed_value] + answer[pos-1][fixed_value+1]) % MOD;
		}
	}

	println!("{}", answer[n-1].iter().sum::<u64>() % MOD);
}