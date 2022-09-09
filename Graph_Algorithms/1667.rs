// Graph_Algorithms/1667.rs
// https://cses.fi/problemset/task/1667


use std::{io, collections::{HashMap, VecDeque}};

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
	let mut connections: HashMap<usize, Vec<usize>> = HashMap::new();
	for _ in 0..m { 
		let r = read_ints(2); 
		connections.entry(r[0]).and_modify(|v| v.push(r[1])).or_insert(vec![r[1]]);
		connections.entry(r[1]).and_modify(|v| v.push(r[0])).or_insert(vec![r[0]]);
	}
	
	let mut route = vec![300000; n+1];
	route[1] = 0;

	let mut next_comps = VecDeque::new();
	if connections.contains_key(&1) { next_comps.push_back(1); }

	let mut step = 0;
	while next_comps.len() > 0 {
		step += 1;
		for _ in 0..next_comps.len() {
			let comp = next_comps.pop_front().unwrap();
			for &conn in &connections[&comp] {
				if route[conn] > step {
					route[conn] = step;
					next_comps.push_back(conn);
				}
			}
		}
	}

	if route[n] == 300000 {
		println!("IMPOSSIBLE");
		return;
	}

	let mut valid_route = vec![n];
	let mut comp = n;
	step = route[n];
	while step > 0 {
		step -= 1;
		for &conn in &connections[&comp] {
			if route[conn] == step {
				valid_route.push(conn);
				comp = conn;
				break;
			}
		}
	}
	
	println!("{}", valid_route.len());
	while let Some(comp) = valid_route.pop() {
		print!("{} ", comp);
	}
}