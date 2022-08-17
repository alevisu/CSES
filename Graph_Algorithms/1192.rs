// Graph_Algorithms/1192.rs
// https://cses.fi/problemset/task/1192

use std::io;

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
	Room(usize),
	Wall,
}

fn main() {
	let (n, m) = { let v = read_ints(2); (v[0], v[1]) };
	let mut map: Vec<Vec<Tile>> = Vec::new();
	let mut line = String::new();
	map.push(vec![Tile::Wall; m+2]);
	for _ in 0..n {
		let mut l = vec![Tile::Wall];
		io::stdin().read_line(&mut line).expect("No input provided");
		for t in line.trim().bytes() { match t {
			b'#' => l.push(Tile::Wall),
			_    => l.push(Tile::Room(0))
		}} 
		assert_eq!(l.len(), m+1, "Wrong input: {}", line);
		l.push(Tile::Wall);
		map.push(l);
		line.clear();
	}
	map.push(vec![Tile::Wall; m+2]);

	fn fill(map: &mut Vec<Vec<Tile>>, x: usize, y: usize, room_number: usize) {
		if let Tile::Room(0) = map[x][y] {
			map[x][y] = Tile::Room(room_number); 
			for dir in [(0, 1), (0, -1), (-1, 0), (1, 0)] {
				fill(map, x+dir.0 as usize, y+dir.1 as usize, room_number)
			}
		}
	}

	let mut total_rooms = 0usize;
	for x in 1..=n { for y in 1..=m {
		if let Tile::Room(0) = map[x][y] {
			total_rooms += 1;
			fill(&mut map, x, y, total_rooms);
		}
	}}

	println!("{}", total_rooms);
	
}