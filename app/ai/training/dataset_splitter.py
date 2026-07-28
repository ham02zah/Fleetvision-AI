from sklearn.model_selection import train_test_split


class DatasetSplitter:
    """
    Splits ML dataset into training and testing sets.
    """

    @staticmethod
    def split(df):

        # Target variable
        y = df["speed"]

        # Features
        X = df.drop(
            columns=[
                "speed",
            ]
        )

        return train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42,
        )