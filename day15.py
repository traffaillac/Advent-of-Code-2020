nums = list(map(int, input().split(',')))
index = {n: i for i, n in enumerate(nums)}
n = 0
for i in range(30_000_000-len(nums)):
	if i%1_000_000==0:
		print(i)
	cur,l = n,len(nums)
	n = l - index.get(n, l)
	index[cur] = l
	nums.append(cur)
print(nums[-1])
