import tensorflow as tf

import Question3.project_config as config
from Question3.model.basic_model import BasicModel
from Question3.model.modified_model import ModifiedModel


class TrainModel:
    def __init__(self, container):
        self.container = container
        self.model = None

    def build_model(self):
        if config.OPTIONAL_MODEL == 1:
            self.model = BasicModel().get_model()
        else:
            self.model = ModifiedModel().get_model()

    def train_model(self):
        self.model.compile(optimizer='adam',
                           loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                           metrics=['accuracy'])
        self.model.fit(self.container.TRAIN_IMAGE,
                       self.container.TRAIN_LABEL, epochs=10)

    def push_model_to_container(self):
        self.container.MODEL = self.model

    def execute(self):
        self.build_model()
        self.train_model()
        self.push_model_to_container()
        return self.container
