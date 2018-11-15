from utilities.parallel_func import run_parallel_funcs
import os

NUM = 1000000


def my_func (args):
	num1 = args[0]
	num2 = args[1]
	num = num1 + num2
	my_list = []
	for i in range(num):
		my_list.append(i)


def parallel(n_proc):

	task_list = []

	for i in range(20):
		num1 = NUM
		num2 = NUM
		args = [num1, num2]
		task = {
			'function': my_func,
			'arguments': args,
		}
		task_list.append(task)

	# n_proc = 4

	run_parallel_funcs(task_list, n_proc)


def sequential():
	for i in range(20):
		num1 = NUM
		num2 = NUM
		args = [num1, num2]
		print(i)
		my_func(args)


# sequential()

# parallel(10)