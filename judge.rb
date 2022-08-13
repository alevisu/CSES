#!/usr/bin/env ruby

class String
	def red;   "\e[31m#{self}\e[0m" end
	def green; "\e[32m#{self}\e[0m" end
	def cyanb; "\e[46m\e[1m#{self}\e[22m\e[0m" end
end

solution = "rustpg/target/debug/rustpg"
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
tests.each { |test|
	testn = test.split(/[-\.]/)[-2]
	result = `#{solution} < #{test}`
	answer = File.read test[0..-4] + 'ans'
	if answer == result 
		nPassed += 1
	else
		puts "\n\n ====> Problem #{problem}: test case ##{testn}: fail".cyanb
		puts ' * Expected:'.green
		puts answer[0..500], ''
		puts ' * Got:'.red
		puts result[0..500]
	end
}

summary = "\n\n ====> Finished: #{nPassed} of #{tests.size} passed"
if nPassed != tests.size 
	summary = summary.red
else
	summary = summary.green
end
puts summary