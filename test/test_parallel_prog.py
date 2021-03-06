import sys
sys.path.append('../')
from utilities.parallel_prog import run_parallel_progs_in_threads as RPPIT,\
	run_parallel_progs_in_processes as RPPIP, run_sequential_progs as RSP
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--size', type=int, default=100)
parser.add_argument('--procs', type=int, default=2)
parser.add_argument('--tasks', type=int, default=2)
args = parser.parse_args()

SIZE = args.size
N_PROC = args.procs
TASKS = args.tasks

cmd_list = []
for i in range(TASKS):
	cmd_list.append('python sleep.py --size {}'.format(SIZE))

n_proc = N_PROC

start = time.time()
RSP(cmd_list)
end = time.time()
# print('sequential =', end - start)
print(end - start)

start = time.time()
RPPIT(cmd_list, n_proc)
end = time.time()
# print('parallel threads =', end - start)
print(end - start)

start = time.time()
RPPIP(cmd_list, n_proc)
end = time.time()
# print('parallel processes =', end - start)
print(end - start)
