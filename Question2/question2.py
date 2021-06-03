import math
from time import time

import matplotlib.pyplot as plt
import numpy
from numpy import random


# Solution 1
def singleNumber_1(nums: list) -> int:
    num_dict = {}
    for element in nums:
        if element not in num_dict:
            num_dict[element] = 1
        else:
            num_dict[element] += 1
    for element in nums:
        if num_dict[element] % 2 == 1:
            return element


# Solution 2
def singleNumber_2(nums: list) -> int:
    ans = 0
    for element in nums:
        ans = (ans ^ element)
    return ans


def generate_test_case() -> list:
    size_of_list = random.randint(10000, 30000)
    if size_of_list % 2 == 0:
        size_of_list += 1
    random_list = list(random.randint(-30000, 30000, size_of_list // 2))
    random_list = random_list + random_list
    random_list.append(random.randint(-30000, 30000))
    random.shuffle(random_list)
    return random_list


def evaluate_time_solution(solution):  # ms
    num_test = 30
    total_time = 0
    for i in range(0, num_test):
        test_case = generate_test_case()
        start_time = time()
        solution(test_case)
        solution_time = (time() - start_time) * 1000
        total_time += solution_time
    return math.log(total_time)


def evaluate_solution(solution):
    num_evaluation = 100
    samples = []
    for i in range(0, num_evaluation):
        samples.append(evaluate_time_solution(solution))
    statistic_for_sample(samples)


def statistic_for_sample(samples):
    print("Sample mean: ", numpy.mean(samples))
    print("Sample variance: ", numpy.var(samples))
    print("Sample std: ", numpy.std(samples))
    print("Sample median: ", numpy.median(samples))
    print("Sample min: ", numpy.min(samples))
    print("Sample max: ", numpy.max(samples))
    print("Q1: ", numpy.quantile(samples, 0.25))
    print("Q2: ", numpy.quantile(samples, 0.5))
    print("Q3: ", numpy.quantile(samples, 0.75))
    print("----------------------------------------------------------")
    plt.xlabel("Log total time")
    plt.hist(samples)
    plt.show()


def main():
    evaluate_solution(singleNumber_1)
    evaluate_solution(singleNumber_2)


if __name__ == '__main__':
    main()
