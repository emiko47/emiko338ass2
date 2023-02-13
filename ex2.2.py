import json
import matplotlib.pyplot as plt
import timeit
import sys
sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

def main():
    with open('ex2.5.json','r') as source:
        arr = json.load(source)

    x_labels = []
    y_labels = []
    for i in arr:
        x_labels.append(len(i))
        y_labels.append(timeit.timeit(lambda: func1(i, 0, (len(i)-1)), number=1))
    
    plt.plot(x_labels, y_labels)
    plt.title("Timing results (ex2.2.py)")
    plt.xlabel("Size of Sub-Array")
    plt.ylabel("Time Taken (seconds)")
    plt.show()




if __name__ == '__main__':
    main()