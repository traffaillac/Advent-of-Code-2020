from sys import stdin

#  NW NE
#    \|
# W - o - E
#     |\
#    SW SE
black = set()
for s in stdin:
	i, x, y = 0, 0, 0
	while i < len(s):
		if s[i] == 'e':
			x += 1
		elif s[i] == 's':
			y += 1
			i += 1
			x += 1 if s[i] == 'e' else 0
		elif s[i] == 'w':
			x -= 1
		elif s[i] == 'n':
			y -= 1
			i += 1
			x -= 1 if s[i] == 'w' else 0
		i += 1
	if (x, y) in black:
		black.remove((x, y))
	else:
		black.add((x, y))
print(len(black))

for i in range(100):
	new = set()
	for x, y in black:
		nb = 0
		for dx, dy in ((-1,-1),(0,-1),(-1,0),(1,0),(0,1),(1,1)):
			if (x+dx, y+dy) in black:
				nb += 1
			elif sum((x+dx+i, y+dy+j) in black for i, j in ((-1,-1),(0,-1),(-1,0),(1,0),(0,1),(1,1))) == 2:
				new.add((x+dx, y+dy))
		if 0 < nb <= 2:
			new.add((x, y))
	black = new
	print(len(black))
