from bisect import bisect_left
from sys import stdin

nums = [int(input()) for i in range(25)]
sums = [sum(nums[:i]) for i in range(len(nums)+1)]
for n in map(int, stdin):
	prev = nums[-25:]
	if all(n-p not in prev for p in prev):
		print(n)
		for i, lo in enumerate(sums):
			j = bisect_left(sums, n+lo)
			if sums[j] == n+lo:
				print(min(nums[i:j])+max(nums[i:j]))
				exit()
	sums.append(sums[-1]+n)
	nums.append(n)
