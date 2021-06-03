from typing import Any


class Container:

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)

    def __init__(self):
        self.TRAIN_IMAGE = None
        self.TRAIN_LABEL = None
        self.TEST_IMAGE = None
        self.TEST_LABEL = None
        self.MODEL = None
        self.LOG_TEST_ACC = None
