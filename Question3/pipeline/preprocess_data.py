class PreprocessDataset:
    def __init__(self, container):
        self.container = container

    def preprocess_data(self):
        self.container.TRAIN_IMAGE = self.container.TRAIN_IMAGE / 255.0
        self.container.TEST_IMAGE = self.container.TEST_IMAGE / 255.0
        self.container.TRAIN_IMAGE = self.container.TRAIN_IMAGE.reshape(self.container.TRAIN_IMAGE.shape[0], 28, 28, 1)
        self.container.TEST_IMAGE = self.container.TEST_IMAGE.reshape(self.container.TEST_IMAGE.shape[0], 28, 28, 1)

    def execute(self):
        self.preprocess_data()
        return self.container
