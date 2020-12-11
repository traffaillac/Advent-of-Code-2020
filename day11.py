from copy import deepcopy
from sys import stdin

seats = list(map(list, stdin.read().split()))
neighbors = [[[] for c in r] for r in seats]
for r, l in enumerate(seats):
	for c, s in enumerate(l):
		for dr, dc in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
			neighbors[r][c].extend(next(([(r+i*dr, c+i*dc)] for i in range(1,len(seats)) if 0<=r+i*dr<len(seats) and 0<=c+i*dc<len(l) and seats[r+i*dr][c+i*dc]!='.'), []))

for i in range(1000000):
	# print('\n'.join(''.join(l) for l in seats), end='\n\n')
	new = deepcopy(seats)
	for r, (S, N) in enumerate(zip(seats, neighbors)):
		for c, (s, n) in enumerate(zip(S, N)):
			if s == '.': continue
			if s == 'L' and all(seats[i][j]!='#' for i, j in n):
				new[r][c] = '#'
			elif s == '#' and sum(seats[i][j]=='#' for i, j in n)>=5:
				new[r][c] = 'L'
	if new == seats:
		break
	seats = new
print(sum(l.count('#') for l in seats))
