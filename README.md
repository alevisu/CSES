# CSES Problem Set Solutions

My solutions for [CSES Problem Set](https://cses.fi/problemset/list/)

Done with Python, C++, Ruby and Rust

Some Python/Ruby solutions not passing runtime limit, but valid

## Scipts

Two scripts to make life a bit easier.

Not crossplatform, works on Linux.

	ruby ./mover.rb
Used internally to move solutions to proper directory in repo

	ruby ./judge.rb [<problem_name>]
Run current build of rust solution, giving it `tests/<problem_name>-*.txt` files as inputs and compare its output to expected output, contained in same files, after separator "`\n---`".

In case those not equal - outputs first 500 chars of actual/expected outputs.

Judge needs `root` privileges once after reboot to create `tmpfs` with 1M size for capturing stderr