#!/usr/bin/env ruby

class String
	def red;   "\e[31m#{self}\e[0m" end
	def green; "\e[32m#{self}\e[0m" end
	def cyanb; "\e[46m\e[1m#{self}\e[22m\e[0m" end
end

solution = "rustpg/target/release/rustpg"
tests_dir = "tests/"

problem = ARGV[0]
if !problem
	puts '', " No problem number provided, aborting ".cyanb, ''
	exit 1
end

tests = Dir[tests_dir + problem + "-*.txt"]

if tests.size != Dir[tests_dir + problem + "-*.ans"].size then
	puts "Number of tests not equal to number of answers for problem #{problem}"
	exit 1
end

nPassed = 0
tests.each_with_index { |test, index|
	testn = test.split(/[-\.]/)[-2]
	puts "\n Testing #{problem}-#{testn} (#{index+1} of #{tests.size})"
	result = `#{solution} < #{test}`
	answer = File.read test[0..-4] + 'ans'
	if answer.strip == result.strip 
		nPassed += 1
		puts "\e[1A\e[KTesting #{problem}-#{testn} (#{index+1} of #{tests.size}): passed".green
	else
		puts "\n\n ====> Problem #{problem}: test case ##{testn}: fail".cyanb
		puts ' * Input: ', test[0..500], ''
		puts ' * Expected:'.green, answer[0..500], ''
		puts ' * Got:'.red, result[0..500]
	end
}

summary = "\n\n ====> Finished: #{nPassed} of #{tests.size} passed"
if nPassed != tests.size 
	summary = summary.red
	puts summary
else
	summary = summary.green
	puts summary, 'Moving solution'
	`./mover.rb`
end