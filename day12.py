from sys import stdin

x, y, dx, dy = 0, 0, 10, 1
for s in stdin:
	v = int(s[1:])
	if s[0] == 'N':
		dy += v
	elif s[0] == 'S':
		dy -= v
	elif s[0] == 'E':
		dx += v
	elif s[0] == 'W':
		dx -= v
	elif s[0] == 'L':
		for i in range(v//90):
			dx, dy = -dy, dx
	elif s[0] == 'R':
		for i in range(v//90):
			dx, dy = dy, -dx
	elif s[0] == 'F':
		x += v*dx
		y += v*dy
print(abs(x)+abs(y))
