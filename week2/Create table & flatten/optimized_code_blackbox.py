def create_table(n: int, m: int) -> list:
    table = [[1 for _ in range(m)] for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            table[i][j] = table[i - 1][j] + table[i][j - 1]
    return table

def flatten(lst: list):
    result = []
    if not isinstance(lst, list):
        return lst
    for element in lst:
        if isinstance(element, list):
            result.extend(flatten(element))
        else:
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