from sys import stdin

def prim(s, i):
	if s[i] == '(':
		i += 1
		res, i = mul(s, i)
		assert s[i] == ')'
		i += 1
	elif s[i].isdigit():
		l = len(s) - i - len(s[i:].lstrip('0123456789'))
		res = int(s[i:i+l])
		i += l
	return res, i

def add(s, i):
	lhs, i = prim(s, i)
	while i<len(s) and s[i]=='+':
		i += 1
		rhs, i = prim(s, i)
		lhs += rhs
	return lhs, i

def mul(s, i):
	lhs, i = add(s, i)
	while i<len(s) and s[i]=='*':
		i += 1
		rhs, i = add(s, i)
		lhs *= rhs
	return lhs, i

print(sum(mul(l.replace(' ', ''), 0)[0] for l in stdin))
