// Graph_Algorithms/1194.rs
// https://cses.fi/problemset/task/1194

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
	Monster(usize),
	Finish,
}

fn main() {
	// Filling map, assigning extra inner boundary tiles as finish tiles
	let (n, m) = { let v = read_ints(2); (v[0], v[1]) };
	let mut map = Vec::new();
	let mut line = String::new();
	let mut hero = BTreeSet::new();
	let mut monsters = BTreeSet::new();
	map.push(vec![Tile::Wall; m+4]);
	map.push(vec![Tile::Finish; m+4]);
	for x in 0..n {
		let mut l = vec![Tile::Wall, Tile::Finish];
		io::stdin().read_line(&mut line).expect("No input provided");
		for (y, t) in line.trim().bytes().enumerate() { match t {
			b'#' =>   l.push(Tile::Wall),
			b'A' => { l.push(Tile::Path(0)); hero.insert((x+2, y+2)); },
			b'M' => { l.push(Tile::Monster(usize::MAX)); monsters.insert((x+2, y+2)); },
			b'.' =>   l.push(Tile::Path(usize::MAX)), 
			_    =>   panic!("Wrong input: {}", line),
		}} 
		assert_eq!(l.len(), m+2, "Wrong input: {}", line);
		l.push(Tile::Finish);
		l.push(Tile::Wall);
		map.push(l);
		line.clear();
	}
	map.push(vec![Tile::Finish; m+4]);
	map.push(vec![Tile::Wall; m+4]);
	
	// Doing BFS
	let mut path: Vec<u8> = Vec::new();
	let mut found = false;
	let mut step = 0;
	let mut path_tile = (0, 0);
	while !found {
		step += 1;
		let mut hero_next = BTreeSet::new();
		let mut monsters_next = BTreeSet::new();
		for tile in monsters {
			for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)] {
				let (x, y) = (tile.0 + dir.0 as usize, tile.1 + dir.1 as usize);
				match map[x][y] {
						Tile::Path(p) => { 
							map[x][y] = Tile::Monster(p);
							monsters_next.insert((x, y));
						},
						_ => (),
				}
			}
		}
		for tile in hero {
			for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)] {
				let (x, y) = (tile.0 + dir.0 as usize, tile.1 + dir.1 as usize);
				match map[x][y] {
					Tile::Path(t) if t > step => { 
						hero_next.insert((x, y)); 
						map[x][y] = Tile::Path(step);
					},
					Tile::Finish => { 
						found = true; 
						path_tile = (tile.0, tile.1); // we have to find previous path point
						break; 
					}
					_ => (),
				}
			}
		}
		monsters = monsters_next;
		hero = hero_next;
		// No accesible path tiles found
		if hero.is_empty() && !found {
			println!("NO"); 
			return;
		}
	}

	// Looking for path
	while step != 0 {
		step -= 1;
		for dir in [(0, 1, b'L'), (1, 0, b'U'), (0, -1, b'R'), (-1, 0, b'D')] {
			let (x, y) = (path_tile.0 + dir.0 as usize, path_tile.1 + dir.1 as usize);
			match map[x][y] {
				Tile::Path(s) => {
					if s != step {continue;}
					path_tile = (x, y);
					path.push(dir.2);
					break;
				},
				Tile::Monster(s) => {
					if s != step {continue;}
					path_tile = (x, y);
					path.push(dir.2);
					break;
				},
				_ => (),
			}
		}
	}
	path.reverse();
	println!("YES\n{}\n{}", path.len(), std::str::from_utf8(&path).unwrap());
}