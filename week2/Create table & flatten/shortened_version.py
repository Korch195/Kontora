def create_table(n, m):
    def calculate_value(i, j):
        return 1 if i == 0 or j == 0 else calculate_value(i - 1, j) + calculate_value(i, j - 1)
    return [[calculate_value(i, j) for j in range(m)] for i in range(n)]

def flatten(lst):
    return lst if not isinstance(lst, list) else [x for sublst in lst for x in (flatten(sublst) if isinstance(sublst, list) else [sublst]) if x is not None]

import tracemalloc
import time

tracemalloc.start()
flatten(create_table(10, 20))
print(tracemalloc.get_traced_memory())
tracemalloc.stop()

start = time.time()
flatten(create_table(10, 20))
end = time.time()
print(end - start)