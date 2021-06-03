import tensorflow as tf


class ImportDataset:
    def __init__(self, container):
        self.container = container
        self.train_images = None
        self.train_labels = None
        self.test_images = None
        self.test_labels = None

    def import_data(self):
        fashion_mnist = tf.keras.datasets.fashion_mnist
        (self.train_images, self.train_labels), (self.test_images, self.test_labels) = fashion_mnist.load_data()

    def push_data_to_container(self):
        self.container.TRAIN_IMAGE = self.train_images
        self.container.TRAIN_LABEL = self.train_labels
        self.container.TEST_IMAGE = self.test_images
        self.container.TEST_LABEL = self.test_labels

    def execute(self):
        self.import_data()
        self.push_data_to_container()
        return self.container
