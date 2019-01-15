import os
import threading
from threading import Thread
from multiprocessing import Process, Array
import multiprocessing
import time

'''
TODO: the main thread keeps one core busy; resolve this issue
'''

def run_parallel_progs_in_threads(cmd_list, n_procs, verbose=False):
	flag = [False for i in range(n_procs)]
	threads = []
	thread_count = 0
	for cmd in cmd_list:
		while(True):
			free_thread_id = -1
			for i in range(n_procs):
				if not flag[i]:
					free_thread_id = i

			if free_thread_id == -1:
				continue
			else:
				flag[free_thread_id] = True
				t =Thread(target=_thread_task, args=(cmd, flag, free_thread_id, verbose, ), name = '{}'.format(thread_count))
				threads.append(t)
				thread_count += 1
				t.start()
				break

	for t in threads:
		t.join()


def _thread_task(cmd, flag, thread_id, verbose):
	name = threading.current_thread().name
	if verbose:
		print('thread start with thread number = {}'.format(name))

	os.system(cmd)

	if verbose:
		print('thread completed with thread number = {}'.format(name))
	flag[thread_id] = False


def run_parallel_progs_in_processes(cmd_list, n_procs, verbose=False):
	# flag = [False for i in range(n_procs)]
	flag = Array('i', n_procs)
	for i in range(n_procs):
		flag[i] = 0
	processes = []
	process_count = 0
	for cmd in cmd_list:
		while(True):
			free_process_id = -1
			for i in range(n_procs):
				if flag[i] == 0:
					free_process_id = i

			if free_process_id == -1:
				continue
			else:
				flag[free_process_id] = 1
				p =Process(target=_process_task, args=(cmd, flag, free_process_id, verbose, ), name ='{}'.format(process_count))
				processes.append(p)
				process_count += 1
				p.start()
				break

	for p in processes:
		p.join()


def _process_task(cmd, flag, process_id, verbose):
	name = multiprocessing.current_process().name
	if verbose:
		print('process start with process number = {}'.format(name))

	os.system(cmd)

	if verbose:
		print('process completed with process number = {}'.format(name))
	flag[process_id] = 0


def run_sequential_progs(cmd_list, verbose=False):
	cmd_count = 0
	for cmd in cmd_list:
		os.system(cmd)
		if verbose:
			print('finished: command number =', cmd_count)
		cmd_count += 1