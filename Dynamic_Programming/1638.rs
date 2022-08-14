// Dynamic_Programming/1638.rs

use std::{io, fmt};//{io, cmp::min};
// const INF: usize = usize::pow(10, 10);
const MOD: usize = usize::pow(10, 9) + 7;

fn read_ints(quantity: usize) -> Vec<usize> {
	let mut line = String::new();
	io::stdin().read_line(&mut line).expect("No input provided");
	let res: Vec<usize> = line.trim().split(char::is_whitespace)
	.map(|s| s.parse().expect("Can't parse this!")).collect();
	if res.len() != quantity { panic!("Wrong quantity of numbers in line") };
	res
}

#[derive(Clone, Debug, Copy)]
enum Cell {
	Square(usize),
	Trap
}
impl fmt::Display for Cell {
	fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
		match self {
			Cell::Trap      => { write!(f, "0") },
			Cell::Square(n) => { write!(f, "{}", n) },
		}
	}
}
type Grid = Vec<Vec<Cell>>;

/// Builts square grid from STDIO
/// 
/// It appends left column and top row with Traps, so
/// numeration starts from 1 `1..=size`
/// 
/// `size` size of a grid
fn make_grid(size: usize) -> Grid {
	let mut grid = vec![vec![Cell::Square(0); size+1]; size+1];
	grid[0] = vec![Cell::Trap; size+1];
	grid[1][1] = Cell::Square(1);
	let mut line = String::new();
	for y in 1..=size {
		grid[y][0] = Cell::Trap;
		io::stdin().read_line(&mut line).expect("Unexpected EOF");
		for (x, c) in line.trim().chars().enumerate() {
			if c == '*' { grid[y][x+1] = Cell::Trap }
		}
		line.clear();
	}
	grid
}


fn main() {
	let n = read_ints(1)[0];
	
	let mut grid = make_grid(n);
	for y in 1..=n {
		for x in 1..=n {
			if let Cell::Trap = grid[y][x] {continue;}
			if let (Cell::Trap, Cell::Trap) = (grid[y-1][x], grid[y][x-1]) {continue;}
			let top = if let Cell::Square(top) = grid[y-1][x] { top } else { 0 };
			let left = if let Cell::Square(left) = grid[y][x-1] { left } else { 0 };
			grid[y][x] = Cell::Square((top + left) % MOD)
		}
	}
		
	// fn show_grid(grid: &Grid) { grid.iter().for_each(|r| println!("{:?}", r)); }
	// show_grid(&grid);
	
	println!("{}", grid[n][n]);
}