n = gets.to_i

combs = Array.new(n+1, 0)
combs[0] = 1
mod = 1e9+7

(1..n).each do |i|
	(1..6).each do |n|
		combs[i] = (combs[i] + combs[i-n]) % mod unless n>i
	end
end

puts combs[n].to_i