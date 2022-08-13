# CSES Problem Set Solutions

My solutions for [CSES Problem Set](https://cses.fi/problemset/list/)

Done with Python, C++, Ruby and Rust

Some Python/Ruby solutions not passing runtime limit, but valid

## Scipts

Two scripts to make life a bit easier.

Not crossplatform, works on Linux.

	ruby ./mover.rb
It happened to be more convinient for me to have a single cargo in `./rustpg/` folder, while making a solution. This script is used to move and rename main.rs to solutions folder based on its first line comment. Look into rust solution files for example.

	ruby ./judge.rb <problem_name>
Run current build of rust solution, giving it `tests/<problem_name>-*.txt` files as inputs and compare its output to `tests/<problem_name>-*.ans`

In case those not equal - outputs first 500 chars of actual/expected outputs.