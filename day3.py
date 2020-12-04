from sys import stdin

grid = [l.rstrip() for l in stdin]
def count(r, c):
	R, C, trees = 0, 0, 0
	while R < len(grid):
		trees += grid[R][C] == '#'
		C = (C+c)%len(grid[R])
		R += r
	return trees
print(count(1,1) * count(1,3) * count(1,5) * count(1,7) * count(2,1))
