// Graph_Algorithms/1193.rs
// https://cses.fi/problemset/task/1193

use std::{io, collections::BTreeSet};

fn read_ints(quantity: usize) -> Vec<usize> {
	let mut line = String::new();
	io::stdin().read_line(&mut line).expect("No input provided");
	let res: Vec<usize> = line.trim().split(char::is_whitespace)
	.map(|s| s.parse().expect("Can't parse this!")).collect();
	if res.len() != quantity { panic!("Wrong quantity of numbers in line") };
	res
}

#[derive(Debug, Clone)]
enum Tile {
	Path(usize),
	Wall,
	Finish,
}

fn main() {
	// Filling map
	let (n, m) = { let v = read_ints(2); (v[0], v[1]) };
	let mut map = Vec::new();
	let mut line = String::new();
	let mut current_step = BTreeSet::new();
	map.push(vec![Tile::Wall; m+2]);
	for x in 0..n {
		let mut l = vec![Tile::Wall];
		io::stdin().read_line(&mut line).expect("No input provided");
		for (y, t) in line.trim().bytes().enumerate() { match t {
			b'#' =>   l.push(Tile::Wall),
			b'A' => { l.push(Tile::Path(0)); current_step.insert((x+1, y+1)); },
			b'B' =>   l.push(Tile::Finish),
			_    =>   l.push(Tile::Path(usize::MAX)),
		}} 
		assert_eq!(l.len(), m+1, "Wrong input: {}", line);
		l.push(Tile::Wall);
		map.push(l);
		line.clear();
	}
	map.push(vec![Tile::Wall; m+2]);
	
	// Doing BFS
	let mut path: Vec<u8> = Vec::new();
	let mut found = false;
	let mut step = 0;
	let mut path_tile = (0, 0);
	while !found {
		step += 1;
		let mut next_step = BTreeSet::new();
		for tile in current_step {
			for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)] {
				let (x, y) = (tile.0 + dir.0 as usize, tile.1 + dir.1 as usize);
				match map[x][y] {
					Tile::Path(t) if t > step => { 
						next_step.insert((x, y)); 
						map[x][y] = Tile::Path(step);
					},
					Tile::Finish => { 
						found = true; 
						path_tile = (x, y); 
						break; 
					}
					_ => (),
				}
			}
		}
		current_step = next_step;
		// No accesible path tiles found
		if current_step.is_empty() && !found {
			println!("NO"); 
			return;
		}
	}

	// Looking for path
	while step != 0 {
		step -= 1;
		for dir in [(0, 1, b'L'), (1, 0, b'U'), (0, -1, b'R'), (-1, 0, b'D')] {
			let (x, y) = (path_tile.0 + dir.0 as usize, path_tile.1 + dir.1 as usize);
			if let Tile::Path(s) = map[x][y] {
				if s != step {continue;}
				path_tile = (x, y);
				path.push(dir.2);
				break;
			} 
		}
	}
	path.reverse();
	println!("YES\n{}\n{}", path.len(), std::str::from_utf8(&path).unwrap());
}