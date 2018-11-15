import os
import threading
from threading import Thread

'''
TODO: the main thread keeps one core busy; resolve this issue
'''

def run_parallel_funcs(task_list, n_processes):
	flag = [n_processes]
	lock = threading.Lock()

	threads = []
	thread_count = 0
	for task in task_list:
		while(True):
			lock.acquire()
			if flag[0] < 0:
				print('*** FLAG less than 0: ERROR ***')
				exit()
			if flag[0] == 0:
				lock.release()
				continue
			else:
				flag[0] += -1
				lock.release()
				t =Thread(target=_thread_task, args=(task, lock, flag,), name = '{}'.format(thread_count))
				threads.append(t)
				print('thread start with thread id = {}'.format(thread_count))
				thread_count += 1
				t.start()
				break

	for t in threads:
		t.join()


def _thread_task(task, lock, flag):
	func = task['function']
	args = task['arguments']
	func(args)

	lock.acquire()
	flag[0] += 1
	print('thread completed with thread id = {}'.format(threading.current_thread().name))
	lock.release()
