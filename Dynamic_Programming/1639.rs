// Dynamic_Programming/1639.rs
// https://cses.fi/problemset/task/1639

use std::io;

fn read_string() -> String {
	let mut line = String::new();
	io::stdin().read_line(&mut line).expect("No input provided");
	line.trim().to_string()
}

fn main() {
	let (src, dst) = (read_string(), read_string());
	
	let mut edit = vec![vec![5001u16; dst.len()+1]; src.len()+1];
	for i in 0..=src.len() {edit[i][0] = i as u16}
	for i in 1..=dst.len() {edit[0][i] = i as u16}

	for (si, sc) in (1..=src.len()).zip(src.chars()) {
		for (di, dc) in (1..=dst.len()).zip(dst.chars()) {
			edit[si][di] = 
				if sc == dc { edit[si-1][di-1] } 
				else { 1 + [edit[si-1][di], edit[si][di-1], edit[si-1][di-1]].iter().min().unwrap() }
		}
	}

	println!("{}", edit[src.len()][dst.len()]);
}