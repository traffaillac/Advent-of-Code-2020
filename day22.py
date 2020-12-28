from sys import stdin

def game(d1, d2):
	rounds = set()
	while d1 and d2:
		r = (tuple(d1), tuple(d2))
		if r in rounds:
			return d1, []
		rounds.add(r)
		c1, c2 = d1.pop(), d2.pop()
		p1 = game(d1[-c1:], d2[-c2:])[0] if len(d1)>=c1 and len(d2)>=c2 else c1>c2
		if p1:
			d1.insert(0, c1)
			d1.insert(0, c2)
		else:
			d2.insert(0, c2)
			d2.insert(0, c1)
	return d1, d2

top, bot = stdin.read().split('\n\n')
D1, D2 = list(map(int, top.split('\n')[:0:-1])), list(map(int, bot.split('\n')[:0:-1]))
d1, d2 = game(D1, D2)
print(sum((i+1)*c for i, c in enumerate(d1 if d1 else d2)))
