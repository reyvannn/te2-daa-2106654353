import sys
import data_read_create as drc

def knapsackDP(values, weights, capacity, i=0, memo=None):
    if memo is None:
        memo = [[None for _ in range(capacity + 1)] for _ in range(len(values) + 1)]
    if memo[i][capacity] is not None:   # Check if value is already calculated in memo
        return memo[i][capacity]
    if i == len(values):        # Base case if we have reached the end of the list
        return 0
    elif capacity < 0:          # Base case if we have exceeded the capacity
        return -sys.maxsize
    else:                       # Recursive case
                                # if we take the item, we add its value and subtract its weight from the capacity, but keep the same index
                                # if we don't take the item, we keep the same capacity, but increase the index
        memo[i][capacity] = max(values[i] + knapsackDP(values, weights, capacity - weights[i], i, memo),
                                 knapsackDP(values, weights, capacity, i + 1, memo))
        return memo[i][capacity]