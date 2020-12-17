from sys import stdin

fields = {}
while l := input():
	name, ranges = l.split(': ')
	r1, r2 = ranges.split(' or ')
	a, b = map(int, r1.split('-'))
	c, d = map(int, r2.split('-'))
	fields[name] = (a, b, c, d)

input() # your ticket:
own = list(map(int, input().split(',')))
sets = [set(name for name,(a,b,c,d) in fields.items() if a<=v<=b or c<=v<=d) for v in own]
input() # \n
input() # nearby tickets
for l in stdin:
	ticket = [set(name for name,(a,b,c,d) in fields.items() if a<=v<=b or c<=v<=d) for v in map(int, l.split(','))]
	if not set() in ticket:
		for s, t in zip(sets, ticket):
			s &= t

while any(sets):
	i, name = next((i, s.pop()) for i, s in enumerate(sets) if len(s)==1)
	for s in sets:
		s.discard(name)
	print(f'{name}: {own[i]}')
