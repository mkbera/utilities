from utilities.parallel_func import run_parallel_funcs_in_threads as RPFIT, run_parallel_funcs_in_processes as RPFIP
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
	return ans

def parallel_threads(n_proc):
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
	RPFIT(task_list, n_proc, verbose=False)


def parallel_processes(n_proc):
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
	RPFIP(task_list, n_proc, verbose=False)


def sequential():
	for i in range(TASKS):
		num1 = NUM
		num2 = NUM
		args = [num1, num2]
		# print(i)
		ans = my_func(args)


start = time.time()
sequential()
end = time.time()
print('sequential = ', end-start)

start = time.time()
parallel_threads(N_PROC)
end = time.time()
print('parallel_threads = ', end-start)

start = time.time()
parallel_processes(N_PROC)
end = time.time()
print('parallel_processes = ', end-start)
