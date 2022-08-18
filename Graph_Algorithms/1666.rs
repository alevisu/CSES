// Graph_Algorithms/1666.rs
// https://cses.fi/problemset/task/1666


use std::{io, collections::HashMap};

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
	let mut roads: HashMap<usize, Vec<usize>> = HashMap::new();
	for _ in 0..m { 
		let r = read_ints(2); 
		roads.entry(r[0]).and_modify(|v| v.push(r[1])).or_insert(vec![r[1]]);
		roads.entry(r[1]).and_modify(|v| v.push(r[0])).or_insert(vec![r[0]]);
	}
	
	fn visit(visited: &mut Vec<bool>, roads: &mut HashMap<usize, Vec<usize>>, city: usize) {
		visited[city] = true;
		if let Some(connected_cities) = roads.get(&city) {
			for city in connected_cities.to_vec() {
				if !visited[city] { visit(visited, roads, city) }
			}
		}
	}

	let mut visited = vec![false; n+1];
	let mut winners = Vec::new();
	for city in 1..=n {
		if visited[city] { continue }
		winners.push(city);
		visit(&mut visited, &mut roads, city);
	}

	println!("{}", winners.len()-1);
	for i in 1..winners.len() {
		println!("{} {}", winners[i-1], winners[i])
	}
}