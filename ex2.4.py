import json
import matplotlib.pyplot as plt
import timeit
import sys
import numpy as np

sys.setrecursionlimit(20000)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = np.median(array[start:end+1])
    low = start
    high = end
    while low <= high:
        while array[low] < p:
            low += 1
        while array[high] > p:
            high -= 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
            low += 1
            high -= 1
    return low

def main():
    with open('ex2.json','r') as source:
        arr = json.load(source)

    x_labels = []
    y_labels = []
    for i in arr:
        x_labels.append(len(i))
        result = timeit.timeit(lambda: func1(i, 0, (len(i)-1)), number=1)
        y_labels.append(result)

    plt.plot(x_labels, y_labels)
    plt.title("Timing results (ex2.4.py)")
    plt.xlabel("Size of Sub-Array")
    plt.ylabel("Time Taken (seconds)")
    plt.show()


if __name__ == '__main__':
    main()
