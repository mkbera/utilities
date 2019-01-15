import os
from itertools import product

size = [10**i for i in range(9)]
procs = [2, 4, 8, 16]
tasks = [2**i for i in range(9)]


try:
	os.makedirs('output/progs/')
except:
	print('dirs already present')

try:
	os.makedirs('output/funcs/')
except:
	print('dirs already present')



for s, p, t in product(size, procs, tasks):
	args = '--size {} --procs {} --tasks {}'.format(s,p,t)

	out = 'output/progs/out_{}_{}_{}'.format(s,p,t)
	command = 'python test_parallel_prog.py {} > {}'.format(args, out)
	os.system(command)

	out = 'output/funcs/out_{}_{}_{}'.format(s,p,t)
	command = 'python test_parallel_func.py {} > {}'.format(args, out)
	os.system(command)


	