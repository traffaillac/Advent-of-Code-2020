from sys import stdin

graph = {} # key=bag name, value=tuple (parents, children)
for l in stdin:
	parent, inner = l.rstrip().split(' bags contain ')
	_, children = graph.setdefault(parent, ([], {}))
	if inner == 'no other bags.':
		continue
	for item in inner.split(', '):
		count, child = item.rsplit(' ', 1)[0].split(' ', 1)
		parents, _ = graph.setdefault(child, ([], {}))
		children[child] = int(count)
		parents.append(parent)

fifo, seen = ['shiny gold'], set()
while fifo:
	bag = fifo.pop(0)
	for p in graph[bag][0]:
		if p not in seen:
			seen.add(p)
			fifo.append(p)
print(len(seen))

def recurse(bag):
	return sum((recurse(child)+1)*count for child, count in graph[bag][1].items())
print(recurse('shiny gold'))
