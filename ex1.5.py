import timeit
import matplotlib.pyplot as plt

# Improved Fibonacci Pseudocode
def func1(n, memo={}):
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    else:
        memo[n] = func1(n-1, memo) + func1(n-2, memo)
        return memo[n]

# Original Fibonacci Pseudocode
def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

#Store the results
results_impro = []
results_orig = []

for i in range(36):
    impro_time = timeit.timeit(lambda: func1(i), number=1)
    results_impro.append(impro_time)

for i in range(36):
    orig_time = timeit.timeit(lambda: func(i), number=1)
    results_orig.append(orig_time)
    

# Plot the results
plt.plot(results_orig, label="Original Fibonacci", color="blue")
plt.plot(results_impro, label="Improved Fibonacci", color="red")
plt.xlabel("Value of n")
plt.ylabel("Time (s)")
plt.title("Time Comparison of the Algorithms")
plt.legend()
plt.show()
