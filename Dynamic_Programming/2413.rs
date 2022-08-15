// Dynamic_Programming/2413.rs
// https://cses.fi/problemset/task/2413

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

// Those are possible interceptions between blocks
//     |           |          |                     |         |                          
// 0 --o--     1   o--    2 --o      3 --o--    4   o     5 --o--     6 --o--    7   o
//     |           |          |          |          |                                 
// Bottom == 0..=7
// Top    == 3 || 6
// 0..=4 --> (0..=5) && !3
// 5..=7 --> 3, 6, 7

fn main() {
	let number_of_tests = read_ints(1)[0];
	let mut tests: Vec<usize> = Vec::new();
	for _ in 0..number_of_tests { tests.push(read_ints(1)[0])}

	let maximum_height = *tests.iter().max().unwrap();
	let mut options = vec![vec![0u64; 8]; maximum_height+1];
	options[0].fill(1);  // filling bottom

	for height in 1..maximum_height {
		for option in 0..=7 {
			if option < 5 {
				for compl in [0, 1, 2, 4, 5] { options[height][option] += options[height-1][compl] }
			} else {
				for compl in [3, 6, 7] { options[height][option] += options[height-1][compl] }
			}
			options[height][option] = options[height][option] % MOD;
		}
	}

	for height in tests {
		println!("{}", (options[height-1][3] + options[height-1][6]) % MOD) // 3 || 6 == top == answer
	}
}