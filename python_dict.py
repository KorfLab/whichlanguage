# memorize one file (the smaller one takes less memory)
vals = {}
with open('unique.txt') as fp:
	for line in fp:
		name, val = line.split()
		vals[name] = val
		
with open('names.txt') as fp:
	for line in fp:
		name, idx = line.split()
		if name in vals:
			print(name, vals[name], idx)
