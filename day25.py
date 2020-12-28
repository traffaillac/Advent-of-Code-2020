sizes = [None] * 20201227
i, n = 0, 1
while sizes[n] == None:
	sizes[n] = i
	n = n * 7 % 20201227
	i += 1
card = sizes[int(input())]
door = sizes[int(input())]
print(pow(pow(7, card, 20201227), door, 20201227))
