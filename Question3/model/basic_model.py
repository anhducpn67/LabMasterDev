import tensorflow as tf


class BasicModel:
    def __init__(self):
        self.model = tf.keras.Sequential([
            tf.keras.layers.Flatten(input_shape=(28, 28)),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(10)
        ])

    def get_model(self):
        return self.model
