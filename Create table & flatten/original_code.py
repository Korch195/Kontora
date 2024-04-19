'''module that consists of two functions'''
def create_table(n: int, m: int) -> list:
    def calculate_value(i, j):
        if i == 0 or j == 0:
            return 1
        return calculate_value(i - 1, j) + calculate_value(i, j - 1)
    table = [[calculate_value(i, j) for j in range(m)] for i in range(n)]
    return table
def flatten(lst: list):
    if not isinstance(lst, list):
        return lst

    result = []
    for element in lst:
        if isinstance(element, list):
            result.extend(flatten(element))
        elif element is not None:
            result.append(element)
    return result

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
