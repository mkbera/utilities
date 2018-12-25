import time

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

start = time.time()
# my_func()

end = time.time()
print('TIME', end - start)