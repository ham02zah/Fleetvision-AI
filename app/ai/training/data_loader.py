import pandas as pd


class DataLoader:
    """
    Loads processed dataset.
    """

    @staticmethod
    def load(path: str):

        df = pd.read_csv(path)

        return df