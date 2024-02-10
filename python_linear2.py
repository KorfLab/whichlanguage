# all file operations, outer loop smaller
with open('unique.txt') as fp1:
	for line in fp1:
		name1, idx = line.split()
		
		with open('names.txt') as fp2:
			for line in fp2:
				name2, val = line.split()
				if name1 == name2: print(name1, val, idx)