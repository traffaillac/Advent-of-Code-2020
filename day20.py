# corners were found by counting occurences of borders: 1693 1109 2909 3371
# each tile is a tuple (top, right, bot, left, img)
left2tile = {}
top2tile = {}
while True:
	num = int(input().split()[1][:-1])
	tile = [input() for i in range(10)]
	t, l = tile[0], ''.join(r[0] for r in tile)
	b, r = tile[9], ''.join(r[9] for r in tile)
	T, L, B, R = t[::-1], l[::-1], b[::-1], r[::-1]
	if num == 1693:
		start = ((t,r,b,l), (L,t,R,b), (B,L,T,R), (r,B,l,T), (T,l,B,r), (l,b,r,t), (b,R,t,L), (R,T,L,B))
	# original tile
	left2tile.setdefault(l, []).append((t, r, b, l, [r[1:9] for r in tile[1:9]]))
	top2tile.setdefault(t, []).append((t, r, b, l, [r[1:9] for r in tile[1:9]]))
	# rotated 90° CW
	left2tile.setdefault(b, []).append((L, t, R, b, [''.join(r[c] for r in tile[8:0:-1]) for c in range(1,9)]))
	top2tile.setdefault(L, []).append((L, t, R, b, [''.join(r[c] for r in tile[8:0:-1]) for c in range(1,9)]))
	# rotated 180° CW
	left2tile.setdefault(R, []).append((B, L, T, R, [r[8:0:-1] for r in tile[8:0:-1]]))
	top2tile.setdefault(B, []).append((B, L, T, R, [r[8:0:-1] for r in tile[8:0:-1]]))
	# rotated 90° CCW
	left2tile.setdefault(T, []).append((r, B, l, T, [''.join(r[c] for r in tile[1:9]) for c in range(8,0,-1)]))
	top2tile.setdefault(r, []).append((r, B, l, T, [''.join(r[c] for r in tile[1:9]) for c in range(8,0,-1)]))
	# flipped with top axis pivot
	left2tile.setdefault(r, []).append((T, l, B, r, [r[8:0:-1] for r in tile[1:9]]))
	top2tile.setdefault(T, []).append((T, l, B, r, [r[8:0:-1] for r in tile[1:9]]))
	# flipped with top-left axis pivot
	left2tile.setdefault(t, []).append((l, b, r, t, [''.join(r[c] for r in tile[1:9]) for c in range(1,9)]))
	top2tile.setdefault(l, []).append((l, b, r, t, [''.join(r[c] for r in tile[1:9]) for c in range(1,9)]))
	# flipped with left axis pivot
	left2tile.setdefault(L, []).append((b, R, t, L, [r[1:9] for r in tile[8:0:-1]]))
	top2tile.setdefault(b, []).append((b, R, t, L, [r[1:9] for r in tile[8:0:-1]]))
	# flipped with top-right axis pivot
	left2tile.setdefault(B, []).append((R, T, L, B, [''.join(r[c] for r in tile[8:0:-1]) for c in range(8,0,-1)]))
	top2tile.setdefault(R, []).append((R, T, L, B, [''.join(r[c] for r in tile[8:0:-1]) for c in range(8,0,-1)]))
	try: input()
	except: break

img = []
t, r, b, l, tile = next(top2tile[t][0] for t,r,b,l in start if len(left2tile[l])==1 and len(top2tile[t])==1)
while True:
	img.extend(['']*8)
	while True:
		for i in range(8):
			img[-8+i] += tile[i]
		if len(left2tile[r])==1:
			break
		r, l, tile = next((R, L, tile) for _,R,_,L,tile in left2tile[r] if R!=l)
	if len(top2tile[b])==1:
		break
	t, r, b, l, tile = next((T, R, B, L, tile) for T,R,B,L,tile in top2tile[b] if B!=t)

def roughness(pic):
	waves = {(r,c) for r in range(len(pic)) for c in range(len(pic[0])) if pic[r][c]=='#'}
	for r in range(len(pic)-2):
		for c in range(len(pic[r])-19):
			monster = {(r+y,c+x) for x,y in ((0,1),(1,2),(4,2),(5,1),(6,1),(7,2),(10,2),(11,1),(12,1),(13,2),(16,2),(17,1),(18,0),(18,1),(19,1)) if pic[r+y][c+x]=='#'}
			if len(monster)==15:
				waves -= monster
	return len(waves)

for i in range(2):
	for j in range(4):
		print(roughness(img))
		img = [''.join(r[c] for r in img[::-1]) for c in range(len(img[0]))]
	img = img[::-1]
