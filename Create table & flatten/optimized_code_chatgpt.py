def create_table(n, m):
    table = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                table[i][j] = 1
            else:
                table[i][j] = table[i - 1][j] + table[i][j - 1]
    return table

def flatten(lst):
    if not isinstance(lst, list):
        return lst
    result = []
    stack = [iter(lst)]

    while stack:
        item = next(stack[-1], None)
        if item is None:
            stack.pop()
        elif isinstance(item, list):
            stack.append(iter(item))
        else:
            result.append(item)
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