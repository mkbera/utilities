from utilities.parallel_func import run_parallel_funcs_in_threads as RPFIT,\
	run_parallel_funcs_in_processes as RPFIP, run_sequential_funcs as RSF
import os
import time

NUM = 10000000
TASKS = 10
N_PROC = 10


def my_func (args):
	num1 = args[0]
	num2 = args[1]
	num = num1 + num2
	ans = 0
	for i in range(num):
		ans += i

task_list = []
for i in range(TASKS):
	num1 = NUM
	num2 = NUM
	args = [num1, num2]
	task = {
		'function': my_func,
		'arguments': args,
	}
	task_list.append(task)


start = time.time()
RSF(task_list)
end = time.time()
print('sequential = ', end-start)

start = time.time()
RPFIT(task_list, N_PROC)
end = time.time()
print('parallel_threads = ', end-start)

start = time.time()
RPFIP(task_list, N_PROC)
end = time.time()
print('parallel_processes = ', end-start)
