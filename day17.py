from sys import stdin

active = {(x,y,0,0) for y,l in enumerate(stdin) for x,s in enumerate(l) if s=='#'}
for i in range(6):
	new = set()
	for x in range(min(x for x,y,z,w in active)-1, max(x for x,y,z,w in active)+2):
		for y in range(min(y for x,y,z,w in active)-1, max(y for x,y,z,w in active)+2):
			for z in range(min(z for x,y,z,w in active)-1, max(z for x,y,z,w in active)+2):
				for w in range(min(w for x,y,z,w in active)-1, max(w for x,y,z,w in active)+2):
					nb = sum((X,Y,Z,W) in active for X in range(x-1,x+2) for Y in range(y-1,y+2) for Z in range(z-1,z+2) for W in range(w-1,w+2))
					if (3<=nb<=4 if (x,y,z,w) in active else nb==3):
						new.add((x,y,z,w))
	active = new
print(len(active))
