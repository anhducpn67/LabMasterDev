import numpy
from matplotlib import pyplot as plt

import project_config as config
from container import Container
from pipeline.evaluate_model import EvaluateModel
from pipeline.import_dataset import ImportDataset
from pipeline.preprocess_data import PreprocessDataset
from pipeline.train_model import TrainModel


def main():
    container = Container()
    container = ImportDataset(container).execute()
    container = PreprocessDataset(container).execute()
    list_acc = []
    for i in range(0, config.NUM_SAMPLES):
        container = TrainModel(container).execute()
        container = EvaluateModel(container).execute()
        list_acc.append(container.LOG_TEST_ACC)
    statistic_for_sample(list_acc)


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


if __name__ == '__main__':
    main()
