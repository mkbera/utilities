''' test multi-processing vs multi-threading '''
import time
from threading import Thread
from multiprocessing import Process

SIZE = 50000000

def my_func ():
	num = SIZE
	my_list = []
	for i in range(num):
		my_list.append(i)

def add ():
	num = SIZE
	ans = 0
	for i in range(num):
		ans += i


def multi_proc():
	p1 = Process(target=add, args=())
	p1.start()
	p1.join()

def multi_thread():
	t1 = Thread(target=add, args=())
	t1.start()
	t1.join()

start = time.time()
# multi_proc()
# multi_thread()
add()
end = time.time()
print('time', end - start)