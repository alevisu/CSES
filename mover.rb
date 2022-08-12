class String
	def red;   "\e[31m#{self}\e[0m" end
	def green; "\e[32m#{self}\e[0m" end
	def cyanb; "\e[46m\e[1m#{self}\e[22m\e[0m" end
end

def prompt(*args)
	print(*args)
	gets.strip
end

original_name = "rustpg/src/main.rs"

new_name = File.open(original_name) { |file| 
	file.readline.split[1]
}

write = 'Y'
if File.exists? new_name then
	write = prompt("\n\n\n=>   Overwrite? #{new_name} (y/N)".red).upcase
end

if write == 'Y' then
	puts "\n\nMoving solution to \"CSES/#{new_name}\"\n\n".green
	`cp #{original_name} #{new_name}`
else
	w = `tput cols`.to_i
	3.times {puts "".center(w).cyanb}
	puts "> Moving was cancelled <".center(w, '-').cyanb
	3.times {puts "".center(w).cyanb}
end