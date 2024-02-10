# memorize one file (the smaller one takes less memory)
names = []
vals = []
with open('unique.txt') as fp:
	for line in fp:
		name, val = line.split()
		names.append(name)
		vals.append(val)
		
with open('names.txt') as fp:
	for line in fp:
		name, idx = line.split()
		if name in names:
			pos = names.index(name)
			val = vals[pos]
			print(name, val, idx)
