import sys
from branchandbound import knapsackBnB
from dynamicprogramming import knapsackDP
import data_read_create as drc
import time
from memory_profiler import memory_usage

def main():
    values, weights, capacity = drc.read('kecil')
    print('Dataset Kecil')

    start_time = time.time()
    start_mem = memory_usage()[0]
    print('Dynamic Programming: ', knapsackDP(values, weights, capacity))
    end_time = time.time()
    end_mem = memory_usage()[0]
    print('Time taken by Dynamic Programming: ', end_time - start_time, 'seconds')
    print('Memory used by Dynamic Programming: ', end_mem - start_mem, 'MB')

    start_time = time.time()
    start_mem = memory_usage()[0]
    print('Branch and Bound: ', knapsackBnB(values, weights, capacity))
    end_time = time.time()
    end_mem = memory_usage()[0]
    print('Time taken by Branch and Bound: ', end_time - start_time, 'seconds')
    print('Memory used by Branch and Bound: ', end_mem - start_mem, 'MB')
    print()

    values, weights, capacity = drc.read('sedang')
    print('Dataset Sedang')

    start_time = time.time()
    start_mem = memory_usage()[0]
    print('Dynamic Programming: ', knapsackDP(values, weights, capacity))
    end_time = time.time()
    end_mem = memory_usage()[0]
    print('Time taken by Dynamic Programming: ', end_time - start_time, 'seconds')
    print('Memory used by Dynamic Programming: ', end_mem - start_mem, 'MB')

    start_time = time.time()
    start_mem = memory_usage()[0]
    print('Branch and Bound: ', knapsackBnB(values, weights, capacity))
    end_time = time.time()
    end_mem = memory_usage()[0]
    print('Time taken by Branch and Bound: ', end_time - start_time, 'seconds')
    print('Memory used by Branch and Bound: ', end_mem - start_mem, 'MB')
    print()

    values, weights, capacity = drc.read('besar')
    print('Dataset Besar')

    start_time = time.time()
    start_mem = memory_usage()[0]
    print('Dynamic Programming: ', knapsackDP(values, weights, capacity))
    end_time = time.time()
    end_mem = memory_usage()[0]
    print('Time taken by Dynamic Programming: ', end_time - start_time, 'seconds')
    print('Memory used by Dynamic Programming: ', end_mem - start_mem, 'MB')

    start_time = time.time()
    start_mem = memory_usage()[0]
    print('Branch and Bound: ', knapsackBnB(values, weights, capacity))
    end_time = time.time()
    end_mem = memory_usage()[0]
    print('Time taken by Branch and Bound: ', end_time - start_time, 'seconds')
    print('Memory used by Branch and Bound: ', end_mem - start_mem, 'MB')

def generate():
    drc.create(100, 'kecil')
    drc.create(1000, 'sedang')
    drc.create(10000, 'besar')

if __name__ == "__main__":
    sys.setrecursionlimit(1000000) # Increase recursion limit
    # generate() # Uncomment this line to generate new data
    main()