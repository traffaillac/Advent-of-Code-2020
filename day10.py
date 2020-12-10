from collections import Counter
from sys import stdin

jolts = [0]+list(sorted(map(int, stdin.readlines())))
diffs = Counter(jolts[i+1]-jolts[i] for i in range(len(jolts)-1))
print(diffs[1] * (diffs[3]+1))
ways = [1]+[0]*jolts[-1] # number of distinct paths from 0 to w
for j in jolts[1:]:
	ways[j] = sum(ways[j-i] for i in range(1, 4) if j-i>=0)
print(ways[-1])
