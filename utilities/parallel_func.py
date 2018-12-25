import os
import threading
from threading import Thread
from multiprocessing import Process
import multiprocessing
import time

'''
TODO: the main thread keeps one core busy; resolve this issue
'''

def run_parallel_funcs_in_threads(task_list, n_processes, verbose=False):
	flag = [False for i in range(n_processes)]
	threads = []
	thread_count = 0
	for task in task_list:
		while(True):
			free_thread_id = -1
			for i in range(n_processes):
				if not flag[i]:
					free_thread_id = i

			if free_thread_id == -1:
				continue
			else:
				flag[free_thread_id] = True
				t =Thread(target=_thread_task, args=(task, flag, n_processes, free_thread_id, verbose, ), name ='{}'.format(thread_count))
				threads.append(t)
				thread_count += 1
				t.start()
				break

	for t in threads:
		t.join()


def _thread_task(task, flag, n_processes, thread_id, verbose):
	name = threading.current_thread().name
	if verbose:
		print('thread start with thread number = {}'.format(name))
	func = task['function']
	args = task['arguments']
	start = time.time()
	ans = func(args)
	end = time.time()
	if verbose:
		print('thread completed with thread number = {}'.format(name))
	flag[thread_id] = False


def run_parallel_funcs_in_processes(task_list, n_processes, verbose=False):
	flag = [False for i in range(n_processes)]
	threads = []
	thread_count = 0
	for task in task_list:
		while(True):
			free_thread_id = -1
			for i in range(n_processes):
				if not flag[i]:
					free_thread_id = i

			if free_thread_id == -1:
				continue
			else:
				flag[free_thread_id] = True
				t =Process(target=_process_task, args=(task, flag, n_processes, free_thread_id, verbose, ), name ='{}'.format(thread_count))
				threads.append(t)
				thread_count += 1
				t.start()
				break

	for t in threads:
		t.join()


def _process_task(task, flag, n_processes, thread_id, verbose):
	name = multiprocessing.current_process().name
	if verbose:
		print('thread start with thread number = {}'.format(name))
	func = task['function']
	args = task['arguments']
	start = time.time()
	ans = func(args)
	end = time.time()
	if verbose:
		print('thread completed with thread number = {}'.format(name))
	flag[thread_id] = False