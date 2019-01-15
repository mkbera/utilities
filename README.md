# utilities
These python scripts help you run programs/functions concurrently. Executing too many programs/functions/threads puts a lot of load on the memory. All the programs keep thrashing each other out of the processor cores. These scripts help you specify the number of processes that you wish to execute concurrently at any given moment on the machine.

parallel programs
-----------------
Use: Run a number of programs in parallel. See example in `test_parallel_prog.py`.
```python
from utilities.parallel_prog import run_parallel_progs_in_threads as RPPIT

cmd_list = ['python prog1.py --arg1_1 <arg1_1v1>',
  'python prog1.py --arg1 <arg1_1v2>',
  'python prog1.py --arg1 <arg1_1v3>',
  'python prog2.py --arg2_1 <arg2_1v1>'] # example cmd_list

RPPIT(cmd_list, n_proc) # cmd_list = the list of commands that you would have run on the command line
  # n_proc = number of processors on the system
```

parallel functions
------------------
Use: Run a number of functions in parallel. See example in `test_parallel_func.py`.
```python
from utilities.parallel_func import run_parallel_funcs_in_threads as RPFIT

def my_func(args): # args = a list containing the arguments
  # code for my func

task1 = {'function': my_func, 'arguments': args_v1}
task2 = {'function': my_func, 'arguments': args_v2}
task3 = {'function': my_func, 'arguments': args_v3}

task_list = [task1, task2, task3] # example task_list

RPFIT(task_list, n_proc) # cmd_list = a list of dictionaries; each dictionaty has a function and its arguments
  # n_proc = number of processors on the system
```

The commands/functions are parallelized using multi-processing. Another way to parallelize would be to use multi-threading. But it was observed that parallelizing through multi-threading is slower than that of multi-processing (marginally slow in case of parallel programs; very slow, even slower than sequential running, in case of parallel functions).
