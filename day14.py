from sys import stdin

mem = {}
for l in stdin:
	left, right = l.rstrip().split(' = ')
	if left == 'mask':
		# mand = int(right.replace('1','0').replace('X','1'), 2)
		# mor = int(right.replace('X','0'), 2)
		X = [i for i in range(len(right)) if right[-1-i]=='X']
		mand = int(right.replace('0','1').replace('X','0'), 2)
		mor = int(right.replace('X','0'), 2)
	else:
		addr, val = int(left[4:-1]) & mand | mor, int(right)
		for i in range(1<<len(X)):
			a = addr
			for bsrc, bdst in enumerate(X):
				a |= ((i >> bsrc) & 1) << bdst
			mem[a] = val
print(sum(mem.values()))
