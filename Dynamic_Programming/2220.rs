// Dynamic_Programming/2220.rs
// https://cses.fi/problemset/task/2220

use std::io;
// const MOD: usize = usize::pow(10, 9) + 7;

fn read_ints(quantity: usize) -> Vec<usize> {
	let mut line = String::new();
	io::stdin().read_line(&mut line).expect("No input provided");
	let res: Vec<usize> = line.trim().split(char::is_whitespace)
	.map(|s| s.parse().expect("Can't parse this!")).collect();
	if res.len() != quantity { panic!("Wrong quantity of numbers in line") };
	res
}


fn main() {
	let (a, b) = { let v = read_ints(2); (v[0], v[1]) };
	
	let mut dp = vec![1usize; 19]; // ceil(log10(b))+1 actually, but w/e
	for i in 1..19 { dp[i] = dp[i-1]*9 }
	
	fn count(n: isize, dp: &Vec<usize>) -> usize {
		if n < 1 { return if n == 0 { 1 } else { 0 } }
		let mut rv = 0;
		let ns: Vec<u8> = n.to_string().bytes().map(|b|b-b'0').collect();
		for i in 0..ns.len() { rv += dp[i] } // for n with less digits

		let mut prev = 0;
		for i in 0..ns.len() {
			let solutions_with_less_digits = dp[ns.len()-i-1];
			let current_digit = ns[i];
			rv += 
				if current_digit == 0 { 0 }
				else { solutions_with_less_digits *
					if prev < current_digit { current_digit-1 } // {set of digits up to current} - {prev}
					else { current_digit } as usize
				};
			if current_digit == prev { return rv } // no point digging further, its already covered
			prev = current_digit
		}
		return rv + 1 // + {n} itself
	}

	println!("{:?}", count(b as isize, &dp) - count(a as isize - 1, &dp));
}