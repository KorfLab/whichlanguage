# all file operations, outer loop larger
with open('names.txt') as fp1:
	for line in fp1:
		name1, idx = line.split()
		
		with open('unique.txt') as fp2:
			for line in fp2:
				name2, val = line.split()
				if name1 == name2: print(name1, val, idx)

