// Dynamic_Programming/1158.rs

use std::{io, cmp::max};

fn read_ints(quantity: usize) -> Vec<usize> {
	let mut line = String::new();
	io::stdin().read_line(&mut line).expect("No input provided");
	let res: Vec<usize> = line.trim().split(char::is_whitespace)
	.map(|s| s.parse().expect("Can't parse this!")).collect();
	if res.len() != quantity { panic!("Wrong quantity of numbers in line") };
	res
}

struct Book {	price: u16,	pages: u16,	id: u16, }

fn main() {
	let (n, x) = { let l = read_ints(2); (l[0] as usize, l[1] as usize)};
	let mut books: Vec<Book> = Vec::new();
	{
		let prices = read_ints(n);
		let pages = read_ints(n);
		for book in 0..n { books.push(Book { price: prices[book] as u16, pages: pages[book] as u16, id: book as u16+1 }) }
	} // free memory
	let mut pages = vec![vec![0u32; x+1]; n+1];
	
	for book in books {
		for money in 1..=x {
			let money_left = money as i32 - book.price as i32;
			let book_and_books_on_money_left = if money_left < 0 
				{ pages[book.id as usize-1][money] } else { pages[book.id as usize-1][money_left as usize] + book.pages as u32 };
			pages[book.id as usize][money] = max(pages[book.id as usize-1][money], book_and_books_on_money_left);
		}
	}

	println!("{}", pages[n][x]);
}