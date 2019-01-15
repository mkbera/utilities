import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--size', type=int, default=None)
args = parser.parse_args()

SIZE = args.size
assert(SIZE is not None)

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
	# print(ans)

start = time.time()
add()
end = time.time()
