import numpy as np
import os

filename = 'random_nums.txt'
location = '/home/hte7ec/workspace/python_learning/test_driven_development/refactoring/'
test_file = os.path.join(location, filename)


def read_ints(file):
    data = []
    with open(file, 'r') as f:
        for line in f:
            data.append(int(line))
    return np.asarray(data)


def count(data):
    return len(data)


def summation(data):
    return np.sum(data)


def average(data):
    return np.average(data)


def minimum(data):
    return np.min(data)


def maximum(data):
    return np.max(data)


def compute_stats(file):
    data = read_ints(file)
    print(f'total = {count(data)}')
    print(f'summation = {summation(data)}')
    print(f'average = {average(data)}')
    print(f'Minimum = {minimum(data)}')
    print(f'Maximum = {maximum(data)}')
    print(f'Harmonic Mean = {harmonic_mean(data)}')


def harmonic_mean(data):
    data = np.asarray(data)  # convert list to array
    if data.size is 0:  # we do not want to divide by zero
        raise ValueError("Data should contain at least one number")
    nominator = count(data)
    denominator = np.sum(1.0 / data)
    return nominator / denominator


def variance(data):
    return np.var(data, ddof=1)


def standard_dev(data):
    return np.std(data, ddof=1)


if __name__ == '__main__':
    compute_stats(test_file)
    data = read_ints(test_file)
