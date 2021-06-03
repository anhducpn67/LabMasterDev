import numpy
from matplotlib import pyplot as plt
from numpy import random


# Estimate PI number
# Area unit circle / Area square = Number inside points / Number total points
# <=> PI / 4 = Number inside points / Number total points
# => PI = (4 * Number inside points) / Number total points
def estimate_PI_number():
    number_samples = 100
    samples = []
    for i in range(0, number_samples):
        num_points = random.randint(20000, 50000)
        inside_points = 0
        for i in range(0, num_points):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            if x * x + y * y <= 1:
                inside_points += 1
        PI_number = (4 * inside_points) / num_points
        samples.append(PI_number)
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
    plt.hist(samples)
    plt.show()


def main():
    estimate_PI_number()


if __name__ == '__main__':
    main()
