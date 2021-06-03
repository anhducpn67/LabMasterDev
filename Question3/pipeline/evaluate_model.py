class EvaluateModel:
    def __init__(self, container):
        self.container = container

    def evaluate_model(self):
        test_loss, test_acc = self.container.MODEL.evaluate(
            self.container.TEST_IMAGE,
            self.container.TEST_LABEL, verbose=2)
        self.container.TEST_ACC = test_acc

    def execute(self):
        self.evaluate_model()
        return self.container
