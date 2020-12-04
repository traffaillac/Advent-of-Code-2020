from string import digits
from sys import stdin

count = 0
for s in stdin.read().split('\n\n'):
	keys = set()
	valid = True
	for p in s.split():
		k, v = p.split(':')
		keys.add(k)
		if k == 'byr':
			valid &= len(v)==4 and v.isdigit() and 1920<=int(v)<=2002
		elif k == 'iyr':
			valid &= len(v)==4 and v.isdigit() and 2010<=int(v)<=2020
		elif k == 'eyr':
			valid &= len(v)==4 and v.isdigit() and 2020<=int(v)<=2030
		elif k == 'hgt':
			unit = v.lstrip(digits)
			v = v[:-len(unit)]
			valid &= v.isdigit() and (150<=int(v)<=193 if unit=='cm' else 59<=int(v)<=76 if unit=='in' else False)
		elif k == 'hcl':
			valid &= v[0]=='#' and len(v)==7 and all(c in '0123456789abcdef' for c in v[1:])
		elif k == 'ecl':
			valid &= v in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
		elif k == 'pid':
			valid &= len(v)==9 and v.isdigit()
	count += valid and {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'} <= keys
print(count)
