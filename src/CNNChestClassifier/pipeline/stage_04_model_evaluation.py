from CNNChestClassifier.config.configuration import ConfigurationManager
from CNNChestClassifier.components.evaluation import Evaluation
from CNNChestClassifier import logger

STAGE_NAME = "Evaluation"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        # evaluation.log_into_mlflow()