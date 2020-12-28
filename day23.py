init = '871369452'
cups = [i+1 for i in range(1_000_000)] # each index points to the following cup
N = len(cups)
for i, j in zip(init, init[1:]):
	cups[int(i)-1] = int(j)-1
if N==len(init):
	cups[int(init[-1])-1] = int(init[0])-1
else:
	cups[int(init[-1])-1] = len(init)
	cups[-1] = int(init[0])-1
c = int(init[0])-1
for i in range(10_000_000):
	if i%1_000_000 == 0:
		print(i)
	c1 = cups[c]
	c2 = cups[c1]
	c3 = cups[c2]
	cups[c] = cups[c3]
	dst = next(i%N for i in range(c-1,c-5,-1) if i%N not in (c1,c2,c3))
	cups[c3] = cups[dst]
	cups[dst] = c1
	c = cups[c]
print((cups[0]+1) * (cups[cups[0]]+1))
