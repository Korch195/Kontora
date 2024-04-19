# importing the module
import tracemalloc

# code or function for which memory
# has to be monitored

# starting the monitoring
tracemalloc.start()

# function call

print(tracemalloc.get_traced_memory())

# The output is given in form of (current, peak).
# Current memory is the memory the code is currently using,
# Peak memory is the maximum space the program used while executing.
 
# stopping the library
tracemalloc.stop()