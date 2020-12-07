from sys import stdin

print(sum(len(set.intersection(*[set(l) for l in s.split()]))
	for s in stdin.read().split('\n\n')))
