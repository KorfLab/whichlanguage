import random
import sys

if len(sys.argv) == 1: sys.exit(f'usage: {sys.argv[0]} <int>') 
limit = int(sys.argv[1])
random.seed(1)

tfp = open('names.txt', 'w')
ufp = open('unique.txt', 'w')
mfp = open('multi.txt', 'w')

for i in range(limit):
    uid = ''.join(random.choices('ABCDEFGHIGJLMNOPQRSTUVWXYZ', k=10))
    tfp.write(f'{uid}\t{i}\n')
    
    if random.random() < 0.1:
        ufp.write(f'{uid}\t{random.random():.4f}\n')
        for i in range(random.randint(1, 3)):
            mfp.write(f'{uid}\t{i + random.random():.4f}\n')

tfp.close()
ufp.close()
mfp.close()