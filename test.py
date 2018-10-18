from utilities.parallel_prog import run_parallel_progs


cmd_list = []

for i in range(20):
	cmd_list.append('python sleep.py')

n_proc = 4

run_parallel_progs(cmd_list, n_proc)