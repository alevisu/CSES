#!/usr/bin/env ruby

solution = "rustpg/target/release/rustpg" # path to executable
solution_source = "rustpg/src/main.rs"    # path to source
tests_dir = "tests/"                      # path to tests
tempdir = '/tmp/ruby-rust-judge'          # tmpfs for capturing STDERR

# ----- Utilities

`mkdir #{tempdir}` unless File.exists? tempdir
`sudo mount tmpfs #{tempdir} -t tmpfs -o size=1M` unless `mount | grep "#{tempdir}"` != ''

require 'tempfile'
def capture_stderr
  backup_stderr = STDERR.dup
  begin
    Tempfile.open("captured_stderr", '/tmp/ruby-rust-judge') do |f|
      STDERR.reopen(f)
      yield
      f.rewind
      f.read
    end
  ensure
    STDERR.reopen backup_stderr
  end
end

class String
	def red;   "\e[31m#{self}\e[0m" end
	def green; "\e[32m#{self}\e[0m" end
	def cyanb; "\e[46m\e[1m#{self}\e[22m\e[0m" end
end

# ----- Judge

problem = ARGV[0]
if !problem
	problem = File.open(solution_source) { |file| 
		/\/(\d+).rs/.match(file.readline)[1]
	}
	puts " * [INFO] No explicit problem provided, assuming current: #{problem}"
end

tests = Dir[tests_dir + problem + "-*.txt"]
puts ' * [INFO] Created symlink to first test', `ln -svf #{__dir__}/#{tests[0]} #{tempdir}/test_input.txt`

nPassed = 0
tests.each_with_index { |test, index|
	testn = test.split(/[-\.]/)[-2]
	puts "\n Testing #{problem}-#{testn} (#{index+1} of #{tests.size})"
	result = ''
	err = capture_stderr { result = `#{solution} < #{test}`	}
	input, expected = File.read(test).split("\n---") 
	if expected.strip == result.strip 
		nPassed += 1
		puts "\e[1A\e[KTesting #{problem}-#{testn} (#{index+1} of #{tests.size}): passed".green
		puts ' => Result:'.green, result[0..500].strip
	else
		puts "\n\n ====> Problem #{problem}: test case ##{testn}: fail".cyanb
		puts '*** Input: ', input[0..500].strip
		puts '*** Expected:'.green, expected[0..500].strip
		puts '*** Got:'.red, result[0..500].strip
		puts "*** Runtime Error:\n#{err}".red unless err == ''
	end
}

summary = "\n ====> Finished: #{nPassed} of #{tests.size} passed"
if nPassed != tests.size || nPassed == 0
	puts "#{summary}#{tests.size != 0 ? '' : ': no tests provided'}".red
else
	puts "#{summary}\n * Moving solution".green
	`./mover.rb`
end