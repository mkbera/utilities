from utilities.parallel_prog import run_parallel_progs_in_threads as RPPIT,\
	run_parallel_progs_in_processes as RPPIP, run_sequential_progs as RSP
import time

SIZE = 20000000
N_PROC = 10
TASKS = 10

cmd_list = []
for i in range(TASKS):
	cmd_list.append('python sleep.py --size {}'.format(SIZE))

n_proc = N_PROC

start = time.time()
RSP(cmd_list)
end = time.time()
print('sequential =', end - start)

start = time.time()
RPPIT(cmd_list, n_proc)
end = time.time()
print('parallel threads =', end - start)

start = time.time()
RPPIP(cmd_list, n_proc)
end = time.time()
print('parallel processes =', end - start)
