#!/usr/bin/env python
# coding: utf-8

import time
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Deterministic QuickSort
def deterministic_quick_sort(arr):
    """Deterministic QuickSort (anchor item is the last in the list)."""
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return deterministic_quick_sort(left) + [pivot] + deterministic_quick_sort(right)

# Randomized QuickSort
def randomized_quick_sort(arr):
    """Randomized QuickSort (reference element is selected randomly)."""
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

# Measuring execution time
def measure_execution_time(sort_function, array, repetitions=5):
    """Measures the average execution time of the sorting algorithm."""
    times = []
    for _ in range(repetitions):
        arr_copy = array.copy()
        start_time = time.time()
        sort_function(arr_copy)
        end_time = time.time()
        times.append(end_time - start_time)
    return np.mean(times)

# Running tests
def run_tests():
    """Runs tests to compare QuickSort."""
    sizes = [10_000, 50_000, 100_000, 500_000]
    results = []

    for size in sizes:
        test_array = np.random.randint(0, 10**6, size).tolist()

        random_quick_time = measure_execution_time(randomized_quick_sort, test_array)
        deterministic_quick_time = measure_execution_time(deterministic_quick_sort, test_array)

        results.append([size, random_quick_time, deterministic_quick_time])
        print(f"Array size: {size}")
        print(f"   Randomized QuickSort: {random_quick_time:.4f} seconds")
        print(f"   Deterministic QuickSort: {deterministic_quick_time:.4f} seconds")

    df_results = pd.DataFrame(results, columns=["Size", "Randomized QuickSort", "Deterministic QuickSort"])
    print("\nTest results:")
    print(df_results)

    return df_results

# Building graphs
def plot_results(df_results):
    """Plots a graph comparing the speed of Randomized and Deterministic QuickSort algorithms."""
    plt.figure(figsize=(10, 5))
    plt.plot(df_results["Size"], df_results["Randomized QuickSort"], marker='o', label="Randomized QuickSort")
    plt.plot(df_results["Size"], df_results["Deterministic QuickSort"], marker='s', label="Deterministic QuickSort")

    plt.xlabel("Array Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Comparison of Randomized and Deterministic QuickSort algorithms")
    plt.legend()
    plt.grid(True)
    plt.show()


# Main
if __name__ == "__main__":
    try:
        df_results = run_tests()
        plot_results(df_results)
    except KeyboardInterrupt:
        print("\nThe program was interrupted by the user (Ctrl+C).")
    except Exception as e:
        print(f"An error occurred: {e}")
