from datetime import datetime


class MetadataBuilder:

    @staticmethod
    def build(metrics):

        return {

            "training_time": datetime.utcnow().isoformat(),

            "framework": "scikit-learn",

            "algorithm": "RandomForestRegressor",

            "metrics": metrics,

        }