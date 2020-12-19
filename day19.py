from sys import stdin

rules = {} # recursive rules
lengths = {} # optimization: all rules have a fixed length
matches = {} # memoising matches
while l := input():
	i, r = l.split(': ')
	if r[0] == '"':
		lengths[int(i)] = 1
		matches[(int(i), r[1])] = True
	else:
		rules[int(i)] = [list(map(int, seq.split())) for seq in r.split(' | ')]

def length(rule):
	if rule in lengths:
		return lengths[rule]
	lengths[rule] = sum(length(r) for r in rules[rule][0])
	return lengths[rule]

def match(rule, msg):
	if rule == 0: # we rely on 0: 8 11 to bypass rules 8 and 11
		l, r = length(42), length(31)
		for i in range(l,len(msg),l):
			# potential bug: 8 and 11 must have 1+ element, not just 0+
			if (len(msg)-i)%r==0 and i//l>(len(msg)-i)//r and \
				all(match(42,msg[j:j+l]) for j in range(0,i,l)) and \
				all(match(31,msg[j:j+r]) for j in range(i,len(msg),r)):
				matches[(0, msg)] = True
				return matches[(0, msg)]
	if length(rule) != len(msg):
		return False
	if (rule, msg) in matches:
		return matches[(rule, msg)]
	if rule not in rules:
		return False
	for seq in rules[rule]:
		assert len(seq)<=2
		l = length(seq[0])
		if match(seq[0], msg[:l]) and (len(seq)==1 or match(seq[1], msg[l:])):
			matches[(rule, msg)] = True
			return True
	matches[(rule, msg)] = False
	return False

print(sum(match(0, m) for m in stdin.read().split()))