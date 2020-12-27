from sys import stdin

allergens = {} # each value is the set of candidate ingredients for each allergen
ingredients = {}
for l in stdin:
	l, r = l.rstrip().split(' (contains ')
	I = set(l.split())
	for i in I:
		ingredients[i] = ingredients.get(i, 0) + 1
	for a in r[:-1].split(', '):
		allergens.setdefault(a, set(I)).intersection_update(I)

dangerous = []
while allergens:
	a, i = next((a, I.pop()) for a, I in allergens.items() if len(I)==1)
	del ingredients[i]
	del allergens[a]
	for s in allergens.values():
		s.discard(i)
	dangerous.append((a, i))

print(sum(ingredients.values()))
print(','.join(map(lambda t:t[1], sorted(dangerous))))
