from sys import stdin

valids = 0
for l in stdin:
	rule, password = l.split(': ')
	nums, letter = rule.split()
	lo, hi = map(int, nums.split('-'))
	# valids += lo <= password.count(letter) <= hi
	valids += (password[lo-1] == letter) ^ (password[hi-1] == letter)
print(valids)
