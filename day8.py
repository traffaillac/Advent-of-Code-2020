from sys import stdin

def run(code):
	seen = [False] * len(code)
	ip, acc = 0, 0
	while 0 <= ip < len(code) and not seen[ip]:
		seen[ip] = True
		inst, arg = code[ip]
		if inst == 'acc':
			acc += arg
			ip += 1
		elif inst == 'jmp':
			ip += arg
		elif inst == 'nop':
			ip += 1
	if ip == len(code):
		print(acc)

code = [(l.split()[0], int(l.split()[1])) for l in stdin]
for i, (inst, arg) in enumerate(code):
	if inst == 'jmp':
		run(code[:i]+[('nop',arg)]+code[i+1:])
	elif inst == 'nop':
		run(code[:i]+[('nop',arg)]+code[i+1:])
