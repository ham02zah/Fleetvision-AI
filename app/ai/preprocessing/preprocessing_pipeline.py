import pandas as pd

from app.ai.preprocessing.data_cleaner import DataCleaner
from app.ai.preprocessing.missing_value_handler import MissingValueHandler
from app.ai.preprocessing.outlier_handler import OutlierHandler
from app.ai.preprocessing.encoder import Encoder


class PreprocessingPipeline:
    """
    Complete preprocessing pipeline.
    """

    @staticmethod
    def process(df: pd.DataFrame) -> pd.DataFrame:

        df = DataCleaner.clean(df)
        df = MissingValueHandler.fill(df)
        df = OutlierHandler.clean(df)
        df = Encoder.encode(df)

        return df

    @staticmethod
    def run(df: pd.DataFrame) -> pd.DataFrame:
        """
        Alias for process().
        """
        return PreprocessingPipeline.process(df)