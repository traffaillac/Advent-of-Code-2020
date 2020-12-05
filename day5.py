from sys import stdin

seats = {int(l.replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0'), 2) for l in stdin}
for s in seats:
	if s+1 not in seats and s+2 in seats:
		print(s+1)
